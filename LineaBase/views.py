
from django.shortcuts import render,redirect
from LineaBase.forms import LineaBaseForm
from django.views import generic
from django.views.generic import UpdateView
from LineaBase.models import LineaBase
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from items.models import Item

# Create your views here.


def LineaBase_view(request):
    form=""
    if request.method=='POST':
        form=LineaBaseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=LineaBaseForm ()

    return render(request, 'LineaBase/agregar_LineaBase.html',{'form':form})



class LineaBaseListView(generic.ListView):
    model = LineaBase
    context_object_name = 'lineabase_list'   # your own name for the list as a template variable
    template_name = 'LineaBase/lista_lineabase.html'  # Specify your own template name/location

    def get_queryset(self):
        return LineaBase.objects.all()



class LineaBaseUpdate(UpdateView):
    model = LineaBase
    fields = ['estado','version','nombre','descripcion','fase','id']
    template_name = 'LineaBase/modificar_lineabase.html'
    success_url=reverse_lazy('listalineabase')

def eliminar_lineabase(request, id):
    lineabase = LineaBase.objects.get(id=id)
    lineabase.delete()
    return redirect('listalineabase')
