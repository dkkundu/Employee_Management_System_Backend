import logging
from sys import _getframe

# DJANGO IMPORTS
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


def media_upload_path(instance, filename):
    """Returns formatted upload to path"""
    path = f'Profile/{instance.id_number}_{instance.first_name}/{filename}'
    logger.debug(  # prints class and function name
        f"{_getframe().f_code.co_name} Media upload path: {path}"
    )
    return path


def media_signature_path(instance, filename):
    """Returns formatted upload to path"""
    path = f'signature/{instance.id_number}_{instance.first_name}/{filename}'
    logger.debug(  # prints class and function name
        f"{_getframe().f_code.co_name} Media upload path: {path}"
    )
    return path


class UserAbstractProfile(models.Model):
    first_name = models.CharField(
        _('First Name'), max_length=255, blank=True, null=True
    )
    last_name = models.CharField(
        _('Family/Last Name'), max_length=255, blank=True, null=True
    )
    nickname = models.CharField(
        _('Nickname'), max_length=255, blank=True, null=True
    )
    id_number = models.CharField(
        _('ID Number'), max_length=30, blank=True, null=True
    )
    phone = models.CharField(
        _('Mobile Phone'), max_length=12, blank=True, null=True,
        validators=[RegexValidator(  # min: 10, max: 12 characters
            r'^[\d]{10,12}$', message='Format (ex: 0123456789)'
        )]
    )
    image = models.ImageField(
        _('Picture'), blank=True, null=True,
        upload_to=media_upload_path
    )
    signature = models.ImageField(
        _('Signature'), blank=True, null=True,
        upload_to=media_signature_path
    )
    bio = models.TextField(
        _('Bio'), blank=True, null=True
    )
    birthday = models.DateField(
        _('Date of Birth'), blank=True, null=True
    )
    gender = models.CharField(
        _('Gender'), max_length=1, blank=True, null=True,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    )
    blood_group = models.CharField(
        _('Blood Group'), max_length=3, blank=True, null=True,
        choices=[
            ('O+', 'O +'),
            ('O-', 'O -'),
            ('A+', 'A +'),
            ('A-', 'A -'),
            ('B+', 'B +'),
            ('B-', 'B -'),
            ('AB+', 'AB +'),
            ('AB-', 'AB -'),

        ]
    )

    joining_date = models.DateField(
        _('Date of Joining'), blank=True, null=True
    )

    @property
    def full_name(self):

        full_name = ''  # default

        if self.first_name:
            full_name = ''.join(self.first_name)
            if self.last_name:
                full_name += f' {self.last_name}'
        else:
            if self.last_name:
                full_name = ''.join(self.last_name)

        return full_name  # returns None if no name is set

    class Meta:
        abstract = True
