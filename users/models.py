
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
"""
There'll be five types of users, 
the Supplier
the Retailer
the Admin
the Health Professional
the Customer

"""



class CustomUserManager(BaseUserManager):
    def create_user(self, email, phoneNumber, isSupplier, isHealthProfessional, password=None):
        if not email:
            raise ValueError('You must have an email to continue')
        if not phone_number:
            raise ValueError('Users must have a phone number to continue')

        user = self.model(
            email=self.normalize_email(email),
            phoneNumber=phone_number,
            isSupplier=isSupplier,
            isHealthProfessional=isHealthProfessional,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone_number, isSupplier=False, isHealthProfessional=False, password=None):
        user = self.create_user(
            email,
            phone_number,
            password=password,
            isSupplier=isSupplier,
            isHealthProfessional=isHealthProfessional
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name  = models.CharField(max_length = 30, blank = True, null =True)
    surname  = models.CharField(max_length = 30, blank = True, null =True)
    email = models.EmailField(verbose_name="email",
                              max_length=200, unique=True)
    phoneNumber = models.CharField(max_length=13)
    isSupplier = models.BooleanField(default=False)
    isHealthProfessional = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    image = models.ImageField(upload_to="files/profiles", blank=True, null=True)
    dateOfBirth = models.DateField(auto_now = False, null = True)
    location = models.TextField()
    objects = CustomUserManager() #fffffff

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class ProfessionalProfile(models.Model):
    available = models.BooleanField(default = True)
    title = models.CharField(max_length = 20)
    qualifications = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    about = models.CharField(max_length=200)

"""supplier might have multiple locations"""
class SupplierLocations(models.Model):
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length = 100)
