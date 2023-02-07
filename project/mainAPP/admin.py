from django.contrib import admin
from .models import Appointment, User
# Register your models here.

admin.site.register([Appointment, User])
