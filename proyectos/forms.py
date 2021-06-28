from django import forms
from proyectos.models import Proyecto

    
class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ( 'nombre','estado',)

        labels={
             'nombre': 'Nombre'
            ,'estado': 'Estado',   
        }  
        widgets={
            'Nombre ': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
        }  