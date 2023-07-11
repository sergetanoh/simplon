from django.urls import path
from .views import *

urlpatterns=[
   # path('',dashboard,name='dashboard'),
    path("",home,name="home"),
    path('ajouter',Add_personne.as_view(),name='ajout-article'),
    path('modifier-personnes/<int:pk>',update_personne.as_view(),name='modif'),
      path('suprimer-article/<int:pk>',delete_personne.as_view(),name='delete'),

]















