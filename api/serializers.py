from rest_framework import serializers
from .models import *

class SinfSerializer(serializers.ModelSerializer):
    class Meta:
        model=SinfInd
        fields="__all__"

class ValerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ValerInd
        fields="__all__"

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administration
        fields="__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields="__all__"

class PosteSerializer(serializers.ModelSerializer):
    sinf=SinfSerializer(read_only=True)
    valeurind=ValerSerializer(read_only=True)
    class Meta:
        model=Poste
        fields="__all__"