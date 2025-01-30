from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class AppUser(User, PermissionsMixin):
    """User model inherited from 'django.contrib.auth.models.User'."""
    def __str__(self):
        return "@{}".format(self.username)
