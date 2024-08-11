from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register("sinf",SinfinV,basename="sinf")
router.register("valerin",ValerinV,basename="valerin")
router.register("administratuion",AdministrationV,basename="administratuion")
router.register("section",SectionV,basename="section")
router.register("poste",PosteV,basename="poste")

urlpatterns = [
    path('',include(router.urls)),
]