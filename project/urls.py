from django.contrib import admin
from django.urls import path
from app.views import clientes, clientesForm, clientesCreate, clientesView, clientesEdit, clientesUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),

    path('clientes/', clientes, name='clientes'),
    path('clientesForm/', clientesForm, name='clientesForm'),
    path('clientesCreate/', clientesCreate, name='clientesCreate'),
    path('clientesView/<int:pk>/', clientesView, name='clientesView'),
    path('clientesEdit/<int:pk>/', clientesEdit, name='clientesEdit'),
    path('clientesUpdate/<int:pk>/', clientesUpdate, name='clientesUpdate'),
]
