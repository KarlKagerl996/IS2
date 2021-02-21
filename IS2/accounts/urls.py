from django.urls  import path

from accounts import views

urlpatterns = [
    #path('login', vie),
    path('login',views.login , name= 'login'),
    path('dashboard',views.dashboard, name= 'dashboard')
]
