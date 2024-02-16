from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_job_title(value):
    if len(value) < 14:
        raise ValidationError(
            _('Job title should be at least 14 characters long.'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(
        max_length=255, validators=[validate_job_title])

    def __str__(self):
        return self.user.username
