from django.db import models


# Create your models here.
class Usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=17)
    perfil = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    login = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

class Clientes (models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=17)
    logradouro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)




