from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Nombre",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    rut = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Rut",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    telefono = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Telefono",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Correo Electronico",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    direccion = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Direccion",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    empresa = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(
                                attrs={
                                    "placeholder": "Empresa",
                                    "class": "form-control is-success is-medium"
                                }
                            ))
    
    class Meta:
        model = Proveedor
        fields = ["nombre", "rut", "telefono", "email", "direccion", "empresa"]


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']