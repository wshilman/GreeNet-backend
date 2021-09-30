from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)

from .models import *

# PATIENT


class PatientCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Patient


class PatientCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Patient

# DOCTOR


class DoctorCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Doctor


class DoctorCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Doctor


# CULTIVATOR

class CultivatorCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Cultivator


class CultivatorCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cultivator

# PATIENTCULTIVATOR


class PatientCultivatorCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = PatientCultivator


class PatientCultivatorCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PatientCultivator
