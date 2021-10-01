from django import shortcuts
from rest_framework.authtoken.models import Token

from .models import *


def makeq(type):
    q = type + '.objects.create_user(**params)'

    return q


def create_token(user):
    token = Token.objects.create(user=user)

    return token


def register_user(params):
    type = params['type']
    params = params.dict()
    params.pop('type')
    user = eval(makeq(type))
    user.save()
    create_token(user)
