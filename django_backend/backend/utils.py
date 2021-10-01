from django import shortcuts
from rest_framework.authtoken.models import Token

from .models import *


def remove_params(params):
    params.pop('type', None)
    params.pop('is_staff', None)
    params.pop('is_superuser', None)


def makeq(type):
    q = type + '.objects.create(**params)'

    return q


def create_token(user):
    token = Token.objects.create(user=user)

    return token


def register_user(params):
    type = params['type']
    params = params.dict()
    remove_params(params)
    user = eval(makeq(type))
    user.save()
    create_token(user)
