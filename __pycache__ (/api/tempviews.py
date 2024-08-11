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
    def get(self, request):
        table = requests.get("http://127.0.0.1:8000/api/poste/")
        datas = table.json()
        for data in datas:
            poste= Postedispo.objects.get(id=data["poste"])
            data["poste"]=poste.nameposte
            sinf=poste.sinf
            sinf=sinf.sinf
            data["posteId"]=poste.id
            if sinf>17:
                sinf="HG"+str(sinf-17)
            data["sinf"]=sinf
            administration=Administration.objects.get(id=int(data["administration"]))
            data["administration"]=administration.name
            section=Section.objects.get(id=int(data['section']))
            data["section"]=section.name
        postedispo=requests.get("http://127.0.0.1:8000/api/postedispo/")
        postesdispo= postedispo.json()
        for post in postesdispo:
            sinf= SinfInd.objects.get(id=int(post["sinf"])) 
            post["sinf"]=sinf.sinf
            post["sinfindice"]=sinf.numind
            print(post)
        administration=requests.get("http://127.0.0.1:8000/api/administratuion/")
        administrations= administration.json()
        section=requests.get("http://127.0.0.1:8000/api/section/")
        section=section.json()

        
        return render(request, 'api/posteaffichage.html', {"data": datas,"dat":postesdispo, "administration":administrations, "section":section })