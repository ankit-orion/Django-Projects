# File: accounts/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if needed

    class Meta:
        # Set the app_label to match the app name if you're using a multi-app setup
        app_label = 'accounts'

# Update CustomUser model to use through models for groups and user_permissions
class CustomUser(AbstractUser):
    # Add custom fields if needed

    groups = models.ManyToManyField(Group, through='CustomUserGroup', related_name='customuser_group_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, through='CustomUserPermission', related_name='customuser_permission_set', blank=True)

    class Meta:
        # Set the app_label to match the app name if you're using a multi-app setup
        app_label = 'accounts'

class CustomUserGroup(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class CustomUserPermission(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
