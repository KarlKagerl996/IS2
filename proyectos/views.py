from django.shortcuts import render,redirect
from proyectos.forms import ProyectoForm
from django.views import generic
from django.views.generic import UpdateView
from proyectos.models import Proyecto
from django.urls import reverse_lazy

# Create your views here.


def proyecto_view(request):
    form=""
    if request.method=='POST':
        form=ProyectoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProyectoForm ()
    
    return render(request, 'proyectos/agregar_proyecto.html',{'form':form})   

    

class ProyectoListView(generic.ListView):
    model = Proyecto
    context_object_name = 'proyecto_list'   # your own name for the list as a template variable
    template_name = 'proyectos/lista_proyectos.html'  # Specify your own template name/location

    def get_queryset(self):
        return Proyecto.objects.all()


class ProyectoUpdate(UpdateView):
    model = Proyecto
    fields = ['nombre','estado']
    template_name = 'proyectos/editar_proyecto.html'
    success_url=reverse_lazy('listaproyectos')

def eliminar_proyecto(request, id):
    project = Proyecto.objects.get(id=id)
    project.delete()
    return redirect('/listaProyectos/')