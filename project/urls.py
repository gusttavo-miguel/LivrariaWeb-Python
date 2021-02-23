from django.contrib import admin
from django.urls import path
from app.views import clientes, clientesForm, clientesCreate, clientesView, clientesEdit, clientesUpdate, \
    clientesDelete, usuarios, usuariosForm, usuariosCreate, usuariosView, usuariosEdit, usuariosUpdate, usuariosDelete, \
    menu

urlpatterns = [
    path('admin/', admin.site.urls),
    # Menu
    path('menu/', menu, name='menu'),

    # Listas
    path('clientes/', clientes, name='clientes'),
    path('usuarios/', usuarios, name='usuarios'),

    # Form
    path('clientesForm/', clientesForm, name='clientesForm'),
    path('usuariosForm/', usuariosForm, name='usuariosForm'),

    # Create
    path('clientesCreate/', clientesCreate, name='clientesCreate'),
    path('usuariosCreate/', usuariosCreate, name='usuariosCreate'),

    # View
    path('clientesView/<int:pk>/', clientesView, name='clientesView'),
    path('usuariosView/<int:pk>/', usuariosView, name='usuariosView'),

    # Edit
    path('clientesEdit/<int:pk>/', clientesEdit, name='clientesEdit'),
    path('usuariosEdit/<int:pk>/', usuariosEdit, name='usuariosEdit'),

    # Update
    path('clientesUpdate/<int:pk>/', clientesUpdate, name='clientesUpdate'),
    path('usuariosUpdate/<int:pk>/', usuariosUpdate, name='usuariosUpdate'),

    # Delete
    path('clientesDelete/<int:pk>/', clientesDelete, name='clientesDelete'),
    path('usuariosDelete/<int:pk>/', usuariosDelete, name='usuariosDelete'),

]
