from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from clientes.models import Cliente

class UserAdminCreationForm(UserCreationForm):

    cpf = forms.CharField(max_length=14, required=True)

    class Meta:
        model = User
        fields = ['username', 'name', 'email','cpf']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']
