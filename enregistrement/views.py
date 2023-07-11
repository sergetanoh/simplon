from django.shortcuts import render,redirect
from .forms import InscriForm
from .models import Inscription
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,DeleteView,CreateView
# Create your views here.


def home(request): # parametre request obligatoire qui va permettre les requettes http
    list_inscrit=Inscription.objects.all() # tu recupere tout les objets de la classe article pour mettre dans list_article
    context={"list_inscrit":list_inscrit}

    return render(request,"acceuil.html",context)


class Add_personne(CreateView):
    model=Inscription
    form_class=InscriForm
    template_name="ajouter.html"
    success_url=""

    def form_valid(self,form): 
        return  super().form_valid(form)
  


class update_personne(UpdateView):
    model=Inscription
    form_class=InscriForm
    template_name="enregis/listconfirm_update.html"


class delete_personne(DeleteView):
    model=Inscription
    success_url='../../'
    template_name="enregis/listconfirm_delete.html"
