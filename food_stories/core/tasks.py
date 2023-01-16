import time
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from celery import shared_task
from core.models import Subsciber
from stories.models import Recipe


@shared_task
def send_mail_to_subscribers():
    subcribers = Subsciber.objects.filter(is_active=True).values_list('email', flat=True)
    recipes = Recipe.objects.all()
    message = render_to_string('email-subscribers.html', {
        'recipes': recipes
    })
    mail = EmailMultiAlternatives(subject='News about our website', body=message, 
                                from_email=settings.EMAIL_HOST_USER, to=subcribers)
    mail.content_subtype = 'html'
    mail.send()
    print('mail sent')




