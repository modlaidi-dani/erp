from rest_framework import serializers
from .models import *
class SinfSerializer(serializers.ModelSerializer):
    class Meta:
        model=SinfInd
        fields="__all__"
class DegrSerializer(serializers.ModelSerializer):
    class Meta:
        model=Degret
        fields="__all__"

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"





class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administration
        fields="__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Section
        fields="__all__"

class PostedispoSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Postedispo
        fields="__all__"

class PosteSerializer(serializers.ModelSerializer):
    valeurind=TableSerializer(read_only=True)

    indice=serializers.IntegerField(source='poste.sinf.numind',read_only=True)
    class Meta:
        model=Poste
        fields="__all__"
