from django import forms
from items.models import Item
from LineaBase.models import LineaBase


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ( 'nombre',
        'descripcion',
        'prioridad',
        'estado',
        'version',)

        labels={
              'estado': 'Estado',
              'version': 'Version',
              'nombre': 'Nombre',
              'descripcion':'Descripcion',
              'fase':'Fase',
        }
        widgets={
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            'Version': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'Fase': forms.TextInput(attrs={'class':'form-control'}),
        }
