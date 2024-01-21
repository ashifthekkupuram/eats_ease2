from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("Name",), max_length=100, blank=True, null=True,)
    username = models.CharField(_("Username",),max_length=255, unique=True, null=True)
    email = models.EmailField(_("Email Address",), max_length=254, unique=True, null=True)
    profile = models.ImageField(default='profile.jpg',upload_to='profiles/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined =  models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.name}"