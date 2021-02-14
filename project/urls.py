from django.contrib import admin
from django.urls import path
from app.views import clientes, clientesForm, clientesCreate, clientesView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),

    path('clientes/', clientes, name='clientes'),
    path('clientesForm/', clientesForm, name='clientesForm'),
    path('clientesCreate/', clientesCreate, name='clientesCreate'),
    path('clientesView/<int:pk>/', clientesView, name='clientesView'),

]
