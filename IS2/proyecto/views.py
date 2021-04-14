from django.shortcuts import render, redirect
from .forms import ProyectoForm
from .models import Proyecto

# Create your views here.

def registrar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/proyecto_form.html',{'form':form})

def listar_proyecto(request):
    proyecto = Proyecto.objects.all().order_by('id')
    return render(request, 'proyecto/listar_proyecto.html',{'Proyectos': proyecto})


def editar_proyecto(request,id_proyecto):
    instancia = Proyecto.objects.get(id=id_proyecto)

    if request.method == "GET":
        form = ProyectoForm(instance=instancia)
    else:
        form = ProyectoForm(request.POST,instance=instancia)
        if form.is_valid():
            form.save()
        return redirect('/listar_proyecto')
    return render(request, 'proyecto/proyecto_form.html',{'form': form})

def eliminar_proyecto(request,id_proyecto):
    proyecto = Proyecto.objects.get(id = id_proyecto)
    proyecto.delete()
    return redirect('/listar_proyecto')
