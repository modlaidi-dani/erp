from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


class SinfinV (viewsets.ModelViewSet):
    queryset= SinfInd.objects.all()
    serializer_class=SinfSerializer

class ValerinV(viewsets.ModelViewSet):
    queryset=Degret.objects.all()
    serializer_class=DegrSerializer

class TableV(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer
    def create(self, request, *args, **kwargs):
        data = request.data 
        degres= Degret.objects.all()
        sinf= SinfInd.objects.get(id=int(data["sinf"]))
        
        i=0
        for degre in degres:

            table=Table.objects.create(
                sinf=sinf,
                degret=degre,
                val=int(data["val"])+i    
            )
            i=table.val
        return Response({"message":"succees"},status=status.HTTP_201_CREATED)
    
class AdministrationV (viewsets.ModelViewSet):
    queryset= Administration.objects.all()
    serializer_class= AdminSerializer

class SectionV(viewsets.ModelViewSet):
    queryset= Section.objects.all()
    serializer_class= SectionSerializer

class PostedispoV(viewsets.ModelViewSet):
    queryset= Postedispo.objects.all()
    serializer_class= PostedispoSerialiser


class PosteV (viewsets.ModelViewSet):
    queryset= Poste.objects.all()
    serializer_class= PosteSerializer
     
    def create(self, request, *args, **kwargs):
        data=request.data

        degret=data["degret"]
        degret=Degret.objects.get(id=int(degret))
        poste=data['poste']
        poste=Postedispo.objects.get(id = int(poste)) 
        sinf = poste.sinf.id
        sinfval=poste.sinf.numind
        print(sinf,  degret)
        table=Table.objects.get(sinf=sinf,degret=degret)
        degretval = table.val
        slairebase=(sinfval+degretval)*45
       
        salairefinale=slairebase+int(data["primeAdministration"])+int(data["primeAutre"])
        print()
        section=Section.objects.get(id =int(data["section"]))
        administration=Administration.objects.get(id=int(data['administration']))
        spotefinal=Poste.objects.create(
            poste=poste,
            degret=degret,
            slairebase= slairebase,
            salairefinale=salairefinale,
            primeAdministration=data["primeAdministration"],
            primeAutre=data["primeAutre"], 
            section=section ,
            administration=administration 

        )
        
        serializer = PosteSerializer(spotefinal)

        
        return Response(serializer.data, status=status.HTTP_201_CREATED )
