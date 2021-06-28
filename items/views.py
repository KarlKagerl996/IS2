from django.shortcuts import render,redirect
from items.forms import ItemForm
from django.views import generic
from django.views.generic import UpdateView
from items.models import Item
from LineaBase.models import LineaBase
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from LineaBase.models import LineaBase


# Create your views here.

def item_add(request, id):
    lineabase = LineaBase.objects.get(id=id)
    item = Item(id_lb=lineabase)
    if request.method=='POST':
        form=ItemForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ItemForm ()
    
    return render(request, 'item/agregar_item.html',{'form':form})
    
class ItemListView(generic.ListView):
    model = Item
    context_object_name = 'item_list'   # your own name for the list as a template variable
    template_name = 'item/lista_items.html'  # Specify your own template name/location

    def get_queryset(self):
        self.linea= get_object_or_404(LineaBase, id=self.kwargs['id_lbase'])
        return Item.objects.filter(id_lb=self.kwargs['id_lbase'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lineabase'] = LineaBase.objects.get(id=self.kwargs['id_lbase'])
        return context
    

class ItemUpdate(UpdateView):
    model = Item
    fields = ['nombre','estado','descripcion','prioridad','version']
    template_name = 'item/modificar_item.html'
    success_url=reverse_lazy('listalineabase')

def eliminar_item(request, id):
    req = Item.objects.get(id=id)
    req.delete()
    return redirect('/listar_lineabase/')