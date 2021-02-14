from django.shortcuts import render, redirect
from app.forms import ClientesForm
from app.models import Clientes
from django.core.paginator import Paginator


#def home(request):

def clientes(request):
    data = {}
    data['db'] = Clientes.objects.all()
    return render(request, 'clientes.html', data)

def clientesForm(request):
    data = {}
    data['form'] = ClientesForm()
    return render(request, 'clientesForm.html', data)

def clientesCreate(resquest):
    form = ClientesForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')

def clientesView(resquest, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(resquest, 'clientesView.html', data)
