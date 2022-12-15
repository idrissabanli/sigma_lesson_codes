from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_gmail(value):
    if not value.endswith('gmail.com'):
        raise ValidationError(_('mail unvani gmail olmalidir'))
    return True
