from django.contrib import admin
from .models import CustomUser, Patient
# Register your models here.
register = admin.site.register(CustomUser)
register = admin.site.register(Patient)
