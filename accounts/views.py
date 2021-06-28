from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserRegisterForm
from django.views import generic
from .models import User
from django.urls import reverse_lazy


# Create your views here.
@login_required()
def home(request):
    return render(request, "home.html")

@login_required()
def logoutUser(request):
    logout(request)
    return redirect('/accounts/login/')

@login_required()
def crear_usuario(request):
    form=""
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserRegisterForm()
    
    return render(request, 'accounts/crear_usuario.html',{'form':form})

class ListarUsuariosView(generic.ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'accounts/listar_usuarios.html'
    success_url = reverse_lazy('listausuarios')
    
    def get_queryset(self):
        return User.objects.all()

class UserUpdate(generic.UpdateView):
    model = User
    fields = [
            'username',
            'first_name',
            'last_name',
            'proyecto',
            'email',
            'cedula',
            'id_rol'
            'telefono',
            'is_staff',
            'is_active',
            'is_superuser',
        ]
    template_name = 'accounts/editar_usuario.html'
    success_url = reverse_lazy('listausuarios')


@login_required()
def eliminar_usuario(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/listar_usuarios/')

@login_required()
def listar_asignar(request):
    context = {'user_list': User.objects.all()}
    return render(request, "accounts/listar_asignar.html", context)

class UpdateProyecto(generic.UpdateView):
    model = User
    fields = [
            'proyecto',
        ]
    template_name = 'accounts/asignar_proyecto.html'
    success_url = reverse_lazy('listarasignar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userr'] = User.objects.get(id=self.kwargs['pk'])
        return context
