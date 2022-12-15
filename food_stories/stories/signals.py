from django.db.models.signals import post_save, m2m_changed
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from stories.models import Recipe


@receiver(post_save, sender=Recipe)
def my_callback(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug_az = slugify(instance.title_az) + '-' + str(instance.id)
        instance.slug_en = slugify(instance.title_en) + '-' + str(instance.id)
        instance.save()
