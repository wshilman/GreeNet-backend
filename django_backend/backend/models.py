from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# TODO fill atributes


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField(_('Birthday'), null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Patient(CustomUser):
    insurance = models.EmailField(_('Obra Social'))

    class Meta:
        verbose_name = _('Paciente')
        verbose_name_plural = _('Pacientes')


class Doctor(CustomUser):

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctores')


class Cultivator(CustomUser):

    class Meta:
        verbose_name = _('Cultivador')
        verbose_name_plural = _('Cultivadores')


class PatientCultivator(CustomUser):

    class Meta:
        verbose_name = _('Paciente Autocultivador')
        verbose_name_plural = _('Pacientes Autocultivadores')


class Relationship(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    cultivator = models.ForeignKey(
        Cultivator, on_delete=models.SET_NULL, null=True)
    patient_cultivator = models.ForeignKey(
        PatientCultivator, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = (
            ('patient', 'doctor', 'cultivator', 'patient_cultivator'), )
        verbose_name = _('Relacion')
        verbose_name_plural = _('Relaciones')
