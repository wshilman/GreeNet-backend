from django.contrib import admin
from .models import *
# Register your models here.
register = admin.site.register(Patient)
register = admin.site.register(Doctor)
register = admin.site.register(Cultivator)
register = admin.site.register(PatientCultivator)
register = admin.site.register(Relationship)
