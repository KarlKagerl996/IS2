from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'id_rol',
            'cedula',
            'telefono',
            'proyecto',
            'is_staff',
            'is_active',
            'is_superuser',
        ]