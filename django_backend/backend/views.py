from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .utils import register_user

# Create your views here.
# TODO [POST] login
# TODO [POST] register
# TODO [GET] list of {all} cultivators
# TODO [GET] list of {all} doctors


class register(APIView):
    # TODO restrict auth

    def post(self, request):
        try:
            params = request.data
            register_user(params=params)
        except Exception as ex:
            print(ex)
            return Response({'message': 'error'})
        else:
            return Response({'message': 'User {0} created'.format(params['email'])})
