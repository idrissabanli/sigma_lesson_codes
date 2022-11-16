from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.tokens import account_activation_token


def send_confirmation_mail(user, current_site):
    message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
    msg = EmailMultiAlternatives(subject='Confirm your account', body=message, 
    from_email='idris.sabanli@gmail.com', to=(user.email,))
    msg.content_subtype = 'html'
    msg.send(fail_silently=True)