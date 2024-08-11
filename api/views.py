from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class SinfinV (viewsets.ModelViewSet):
    queryset= SinfInd.objects.all()
    serializer_class=SinfSerializer
class ValerinV(viewsets.ModelViewSet):
    queryset=ValerInd.objects.all()
    serializer_class=ValerSerializer

class AdministrationV (viewsets.ModelViewSet):
    queryset= Administration.objects.all()
    serializer_class= AdminSerializer

class SectionV(viewsets.ModelViewSet):
    queryset= Section.objects.all()
    serializer_class= SectionSerializer

class PosteV (viewsets.ModelViewSet):
    queryset= Poste.objects.all()
    serializer_class= PosteSerializer
    def create(self, request, *args, **kwargs):
        data=request.data
        sinf= data["sinf"]
        val=data["valeurind"]
        slairebase=(sinf["numind"]+val["val"])*45
        data["slairebase"]=slairebase
        data["salairefinale"]=slairebase+data["primeAdministration"]+data["primeAutre"]