from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField


# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Helps work with custom user manager."""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a user object."""

        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """ Create super user."""

        user = self.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUserProfile(AbstractBaseUser, PermissionsMixin):
    """ User profile model."""

    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Undecided', 'Undecided')
    )

    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    country = CountryField(blank=True, null=True, blank_label='(Select country)')
    occupation = models.CharField(max_length=50, blank=True, null=True)
    phone_number = PhoneField(blank=True, null=True, help_text='Contact phone number')
    photo = models.ImageField(upload_to='users/photos', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
