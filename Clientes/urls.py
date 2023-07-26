from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.clientes, name='crear-cliente'),
    path("proveedores/", views.createProveedor, name='crear-proveedor')
]