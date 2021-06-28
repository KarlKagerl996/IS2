from django import forms
from LineaBase.models import LineaBase
from proyectos.models import Proyecto




class LineaBaseForm(forms.ModelForm):

    class Meta:
        model = LineaBase
        fields = ( 'estado','version','nombre','descripcion','fase','id_proyecto',)

        labels={
              'estado': 'Estado',
              'version': 'Version',
              'nombre': 'Nombre',
              'descripcion':'Descripcion',
              'fase':'Fase',
              'id_proyecto':'Proyecto',

        }
        widgets={
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            'Version': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'Fase': forms.TextInput(attrs={'class':'form-control'}),
            'Proyecto' : forms.ModelChoiceField(queryset=Proyecto.objects.all()),
        }
