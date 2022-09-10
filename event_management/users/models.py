from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import BaseUserManager

class MyCustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, mobile_number):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.username = username
        user.set_password(password)
        user.mobile_number = mobile_number
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, mobile_number):
        user = self.create_user(username, email, password, mobile_number)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    mobile_number = models.CharField(max_length=11, unique=True, default="")
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    objects = MyCustomUserManager()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
