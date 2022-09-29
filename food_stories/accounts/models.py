from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('Sekil', null=True, blank=True, upload_to='media/user_profile')
    bio = models.TextField(null=True, blank=True)

