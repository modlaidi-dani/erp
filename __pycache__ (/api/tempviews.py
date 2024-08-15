import requests
from django.shortcuts import render
from django.views import View
from . models import *
class SinfTemp(View):
    def get(self, request):
        # Faire la requête GET
        table = requests.get("http://127.0.0.1:8000/api/table/")
        
        data = table.json()
        respense=[]
        for i in range(1,25):
        
            sinf=SinfInd.objects.get(id=i)
            num=sinf.numind
            filtered_data = [item for item in data if item['sinf'] == i]
            for x in filtered_data:
                x["sinfval"]=num
                respense.append(x)
       
        numbers = range(1, 13)

        return render(request, 'api/table.html', {"data": respense })
class Postetemp(View):
       def get(self,request):
        return render(request, 'api/posteaffichage.html')
class PosteDispoTemp(View):
    def get(self,request):
        return render(request, 'api/poste.html')
