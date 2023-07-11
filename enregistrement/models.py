from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Inscription(models.Model):# forcement heriter de la classe models.model qui est un module python
    # nous allons lister les attributs de notre classe qui vont representer les champs de notre table
    nom=models.CharField(max_length=50) # le titre qui sera en chaine de caractere et qui à pour taille 50
    prenom=models.CharField(max_length=150) # la description aura comme type texte
    numero=models.CharField(max_length=50) # on declare notre image de type image
    email=models.CharField(max_length=300) # la description aura comme type texte
    created_at=models.DateTimeField(auto_now_add=True)# veut dire de mettre la date actuel  lorsqu'on ajoute un element
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom # veut dire que si on veut afficher un element il suffit uniquement du titre dans le cote administrateur quand on 
    # on ajoute un article  c'et le nom ce l'article on vois



    def get_absolute_url(self):
        return reverse("home") 