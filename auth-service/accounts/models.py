from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Invite(models.Model):
    code = models.CharField(max_length=4, verbose_name="Invite code", unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    used_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
