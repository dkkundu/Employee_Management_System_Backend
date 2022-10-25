import logging

# DJANGO IMPORTS
from django.core.validators import RegexValidator
from django.db import models
from address.models import (
    Division,
    District,
    Upazila
)


logger = logging.getLogger(__name__)


class AbstractAddress(models.Model):

    present_division = models.ForeignKey(
        Division, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_present_division',
        null=True, blank=True
    )
    present_district = models.ForeignKey(
        District, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_present_district',
        null=True, blank=True
    )
    present_upazila = models.ForeignKey(
        Upazila, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_present_upazila',
        null=True, blank=True
    )
    present_post_code = models.PositiveIntegerField(
        null=True, blank=True,
        help_text='Numeric 4 digits (ex: 1234)',
        validators=[RegexValidator(
            r"^[\d]{4}$", message='Numeric 4 digits (ex: 1234)'
        )]
    )
    present_address = models.TextField(
        null=True, blank=True, help_text='Ex: 2/17, Mirpur-11'
    )

    # permanent address
    same_as_present_address = models.BooleanField(default=False)
    permanent_division = models.ForeignKey(
        Division, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_permanent_division',
        blank=True, null=True
    )
    permanent_district = models.ForeignKey(
        District, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_permanent_district',
        blank=True, null=True
    )
    permanent_upazila = models.ForeignKey(
        Upazila, models.SET_NULL,
        related_name='%(app_label)s_%(class)s_permanent_upazila',
        blank=True, null=True
    )
    permanent_post_code = models.PositiveIntegerField(
        blank=True, null=True,
        help_text='Numeric 4 digits (ex: 1234)',
        validators=[RegexValidator(
            r"^[\d]{4}$", message='Numeric 4 digits (ex: 1234)'
        )]
    )
    permanent_address = models.TextField(
        blank=True, null=True, help_text='Ex: 2/17, Mirpur-11'
    )

    class Meta:
        abstract = True

    @property
    def get_full_present_address(self):
        save_present_address = ''
        if self.present_address:
            save_present_address = ''.join(self.present_address)
        if self.permanent_upazila:
            save_present_address += f', {self.permanent_upazila} ,'
        if self.present_district:
            save_present_address += f' {self.present_district}'
        if self.present_post_code:
            save_present_address += f' - {self.present_post_code} ,'
        if self.present_division:
            save_present_address += f'{self.present_division} ,'
        save_present_address += 'Bangladesh '

        return save_present_address

    @property
    def get_full_permanent_address(self):
        save_permanent_address = ''  # default
        if self.permanent_address:
            save_permanent_address = ''.join(self.permanent_address)
        if self.permanent_upazila:
            save_permanent_address += f', {self.permanent_upazila} ,'
        if self.permanent_district:
            save_permanent_address += f' {self.permanent_district},'
        if self.permanent_post_code:
            save_permanent_address += f' - {self.permanent_post_code} ,'
        if self.permanent_division:
            save_permanent_address += f'{self.permanent_division} ,'
        save_permanent_address += 'Bangladesh '
        return save_permanent_address
