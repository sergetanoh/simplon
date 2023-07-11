from django import forms
from .models import Inscription

class InscriForm(forms.ModelForm):
    class Meta:
        model=Inscription
        fields=["nom","prenom","numero","email"]
        labels={"nom":"nom","prenom":"prenom","numero":"numero","email":"email"}
        widgets={
            "nom":forms.TextInput(attrs={'class':'form-control'}),
            "prenom":forms.TextInput(attrs={'class':'form-control'}),
            "numero":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.TextInput(attrs={'class':'form-control','rows':5})
        }