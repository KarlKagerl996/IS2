from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from  Usuarios.models import Usuario
from  Roles.models import Rol

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('admin/')
        else: 
            #Para los usuarios que no son admin
            for usuario in Usuario.objects.all():
                if usuario.username==username and usuario.password==password:
                    return redirect('dashboard')       
                else:
                    return redirect('login') 
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
	# Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('')
