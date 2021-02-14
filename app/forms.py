from django.forms import ModelForm
from app.models import Usuarios, Clientes


# Criação de classes de formulários
class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id', 'nome', 'telefone', 'perfil', 'status', 'login', 'senha']


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['cpf', 'nome', 'telefone', 'logradouro', 'cidade', 'UF']
