from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    USUARIOS_ESCOLHAS = [
        ('gest','gestor'),
        ('prof','professores'),
    ]
    usuario = models.CharField(max_length=4, choices=USUARIOS_ESCOLHAS, default='prof')
    biografia = models.TextField(max_length=200, blank=True ,null=True)
    idade = models.PositiveIntegerField(null=True,blank=True)
    telefone = models.CharField(max_length=11,null=True,blank=True)



    def __str__(self):
        return self.username



class Professor(models.Model):
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    ni = models.CharField(max_length=100, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=11,null=True,blank=True)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()
    


    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100, null=False, blank=False)
    curso = models.CharField(max_length=30,null=False)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    professor_responsavel = models.ForeignKey(Professor,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_disciplina

class Ambiente(models.Model):
    periodos_escolha = [
        ('Dia', 'Dia'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=5, choices=periodos_escolha,blank=False,null=False)
    sala_reservada = models.CharField(max_length=500)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, limit_choices_to={'usuario':'prof'})
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.sala_reservada