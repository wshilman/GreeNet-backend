from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .utils import register_user
from .serializers import DoctorSerializer, CultivatorSerializer, PatientCultivatorSerializer
from .models import Doctor, Cultivator, PatientCultivator

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


class get_doctors_list(ListAPIView):

    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all().order_by('id')


class get_cultivators_list(ListAPIView):

    serializer_class = CultivatorSerializer

    def get_queryset(self):
        return Cultivator.objects.all().order_by('id')


class get_patient_cultivators_list(ListAPIView):

    serializer_class = PatientCultivatorSerializer

    def get_queryset(self):
        return PatientCultivator.objects.all().order_by('id')