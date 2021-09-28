from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# TODO fill atributes and relations

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
    pass

class Cultivator(CustomUser):
    pass

class PatientCultivator(CustomUser):
    pass

class Interface(models.Model):
    # many2many
    pass
