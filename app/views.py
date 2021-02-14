from django.shortcuts import render, redirect
from app.forms import UsuariosForm
from app.models import Usuarios
from django.core.paginator import Paginator


def home(request):
    data = {}
    search = request.GET.get('search')
    all = Carros.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    if search:
        data['db'] = Carros.objects.filter(id__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)


def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
