from django.db import models
from core.validators import validate_gmail


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    name = models.CharField('Adiniz', max_length=50)
    email = models.EmailField('E-poct', max_length=30)
    subject = models.CharField('Movzu', max_length=255)
    message = models.TextField('Mesaj')
    
    class Meta:
        verbose_name = 'Elaqe'
        verbose_name_plural = 'Elaqeler'
        ordering = ('-name', 'created_at',)

    def __str__(self):
        return f"{self.name} Subject: {self.subject}"


class Subsciber(AbstractModel):
    email = models.EmailField(max_length=40)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Subcriber'
        verbose_name_plural = 'Subcribers'
        ordering = ('created_at',)
