from rest_framework import serializers

from .models import Doctor, Cultivator, PatientCultivator

fields_in_common = (
            'id',
            'email',
            'username',
            'name',
            'date_of_birth',
            'first_name'
        )


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = fields_in_common


class CultivatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cultivator
        fields = fields_in_common


class PatientCultivatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientCultivator
        fields = fields_in_common