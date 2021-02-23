from django.shortcuts import render, redirect
from app.forms import ClientesForm, UsuariosForm
from app.models import Clientes, Usuarios
from django.core.paginator import Paginator

def menu (request):
    return render(request, 'menu.html')

def clientes(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Clientes.objects.filter(cpf__icontains=search)
    else:
        data['db'] = Clientes.objects.all()

    # all = Clientes.objects.all()
    # paginator = Paginator(all, 5)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)

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


# -------------------------------------------------------------------------------------------#
def usuarios(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Usuarios.objects.filter(id__icontains=search)
    else:
        data['db'] = Usuarios.objects.all()
    return render(request, 'usuarios.html', data)


def usuariosForm(request):
    data = {}
    data['form'] = UsuariosForm()
    return render(request, 'usuariosForm.html', data)


def usuariosCreate(resquest):
    form = UsuariosForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuarios')


def usuariosView(resquest, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    return render(resquest, 'usuariosView.html', data)


def usuariosEdit(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    data['form'] = UsuariosForm(instance=data['db'])
    return render(request, 'usuariosForm.html', data)


def usuariosUpdate(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    form = UsuariosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('usuarios')


def usuariosDelete(request, pk):
    db = Usuarios.objects.get(pk=pk)
    db.delete()
    return redirect('usuarios')
