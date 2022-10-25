import logging

# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


class AbstractBaseFields(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('final', _('Final')),
        ('cancelled', _('Cancelled')),
        ('deleted', _('Deleted')),
        ('active', _('Active')),
        ('inactive', _('Inactive')),
        ('pending', _('Pending')),
        ('rejected', _('Rejected')),
        ('approved', _('Approved')),
        ('published', _('Published')),
        ('unpublished', _('Unpublished')),
    )
    status = models.CharField(
        _('Status'), max_length=20, choices=STATUS_CHOICES, default='draft',
        null=True, blank=True
    )
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_createdby"
    )
    is_active = models.BooleanField(
        _('Is Active'), default=False
    )
    is_deleted = models.BooleanField(
        _('Is Deleted'), default=False
    )
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )

    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_deleted"
    )
    deleted_at = models.DateTimeField(
        _('Deleted At'), blank=True, null=True
    )
    confirm_at = models.DateTimeField(
        _('Confirm At'), blank=True, null=True
    )
    confirm_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_confirmby"
    )

    def soft_delete(self):
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def soft_deactive(self):
        self.is_active = False
        self.save()

    def confirm(self, request):
        if self.status == 'draft':
            self.status = 'final'
            self.confirm_at = timezone.now()
            self.confirm_by = request.user
            self.save()

    def active(self, request):
        if self.status != 'active':
            self.status = 'active'
            self.last_updated = timezone.now()
            self.updated_user = request.user
            self.save()

    def inactive(self, request):
        if self.status == 'active':
            self.status = 'inactive'
            self.last_updated = timezone.now()
            self.updated_user = request.user
            self.save()

    def confirm_final(self, request):
        if self.status == 'draft':
            self.status = 'final'
            self.confirm_at = timezone.now()
            self.confirm_by = request.user
            self.save()

    def cancel(self):
        if self.status == 'draft':
            self.delete()

    class Meta:
        abstract = True
