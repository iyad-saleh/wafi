from django.core.checks.messages import Error
from django.db import models
from .managers import SoftDeleteManager
from django.conf import settings
from company.models import Company
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False, blank=True)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        raise Error()

    class Meta:
        abstract = True
