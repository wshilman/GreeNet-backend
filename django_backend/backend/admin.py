from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *


class PatientCustomUserAdmin(UserAdmin):
    form = PatientCustomUserCreationForm
    add_form = PatientCustomUserCreationForm


class DoctorCustomUserAdmin(UserAdmin):
    form = DoctorCustomUserCreationForm
    add_form = DoctorCustomUserCreationForm


class CultivatorCustomUserAdmin(UserAdmin):
    form = CultivatorCustomUserCreationForm
    add_form = CultivatorCustomUserCreationForm


class PatientCultivatorCustomUserAdmin(UserAdmin):
    form = PatientCultivatorCustomUserCreationForm
    add_form = PatientCultivatorCustomUserCreationForm


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Patient, PatientCustomUserAdmin)
admin.site.register(Doctor, DoctorCustomUserAdmin)
admin.site.register(Cultivator, CultivatorCustomUserAdmin)
admin.site.register(PatientCultivator, PatientCultivatorCustomUserAdmin)
admin.site.register(Relationship)
