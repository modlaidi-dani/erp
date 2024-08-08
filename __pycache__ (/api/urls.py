from django.urls import path,include
from rest_framework import routers
from .views import *
from .tempviews import SinfTemp , Postetemp
router = routers.DefaultRouter()
router.register("sinf",SinfinV,basename="sinf")
router.register("valerin",ValerinV,basename="valerin")
router.register("administratuion",AdministrationV,basename="administratuion")
router.register("section",SectionV,basename="section")
router.register("poste",PosteV,basename="poste")
router.register("postedispo",PostedispoV,basename="postedispo")
router.register("table",TableV,basename="table")


urlpatterns = [
    path('',include(router.urls)),
    path('sinftemp/', SinfTemp.as_view() , name='sinftemp'),
    path('postetemp/', Postetemp.as_view() , name='postetemp'),
    

]