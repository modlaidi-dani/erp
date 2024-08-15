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
    catigory=serializers.CharField(source='sinf.sinf',read_only=True )	
    indiceM=serializers.CharField(source='sinf.numind',read_only=True )	
    class Meta:
        model=Postedispo
        fields="__all__"

class PosteSerializer(serializers.ModelSerializer):
    nameposte=serializers.CharField(source='poste.nameposte',read_only=True)
    catigory=serializers.CharField(source='poste.sinf.sinf',read_only=True )	
    indice=serializers.IntegerField(source='poste.sinf.numind',read_only=True)
    administration= serializers.CharField(source='administration.name')
    section=serializers.CharField(source="section.name")
    class Meta:
        model=Poste
        fields="__all__"
