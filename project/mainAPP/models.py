# from django.db import models
#
# # Create your models here.
# from django.contrib.auth.models import User
# from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def _str_(self):
        return self.email

    class Meta:
        verbose_name_plural = "User Accounts"

# class UserProfileManager(BaseUserManager):
#     """helps django work with our custom user model"""
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('User must have email')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """creates and saves a new superuser with given details"""
#         user = self.create_user(email, username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return self.email

# class UserProfileManager(BaseUserManager):
#     """helps django work with our custom user model"""
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('User must have email')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """creates and saves a new superuser with given details"""
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     admin = models.BooleanField(default=False)  # a superuser
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     def __str__(self):
#         return self.email
#
#     objects = UserProfileManager()
#
#     def natural_key(self):
#         return (self.username,)
#
#     @property
#     def is_staff(self):
#          # "Is the user a member of staff?"
#          return self.staff
#
#     @property
#     def is_admin(self):
#          # "Is the user a admin member?"
#          return self.admin
#
#     @property
#     def is_active(self):
#          # "Is the user active?"
#          return self.active
#
#     class Meta:
#         unique_together = (("username", "email"),)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')

    def __str__(self):
        return self.name
