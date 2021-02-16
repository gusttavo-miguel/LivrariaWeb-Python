from django.shortcuts import render, redirect
from app.forms import ClientesForm
from app.models import Clientes
from django.core.paginator import Paginator


# def home(request):

def clientes(request):
    data = {}
    #data['db'] = Clientes.objects.all()
    search = request.GET.get('search')

    all = Clientes.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
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


def clientesEdit(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    data['form'] = ClientesForm(instance=data['db'])
    return render(request, 'clientesForm.html', data)


def clientesUpdate(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    form = ClientesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('clientes')


def clientesDelete(request, pk):
    db = Clientes.objects.get(pk=pk)
    db.delete()
    return redirect('clientes')
