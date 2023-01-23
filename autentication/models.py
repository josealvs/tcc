from django.db import models
from django.contrib.auth.models import User
        
class projetos(models.Model):
    titulo = models.CharField(max_length=45)
    data_inicio = models.DateTimeField()
    descricao = models.TextField(max_length=500)
    orientador = models.ForeignKey(User, related_name = 'orientador', on_delete = models.CASCADE, default = None, null = True)
    aluno = models.ForeignKey(User, related_name = 'aluno', on_delete = models.CASCADE, default = None, null = True)
    def __str__(self):
        return self.titulo


class atividades(models.Model):
    descricao = models.TextField(max_length=100)
    status = models.ForeignKey("status", on_delete=models.CASCADE, default=None, null=True)
    orientador = models.ForeignKey(User, related_name = 'orientador_atividade', on_delete = models.CASCADE, default = None, null = True)
    aluno = models.ForeignKey(User, related_name = 'aluno_atividade', on_delete = models.CASCADE, default = None, null = True)
    projeto = models.ForeignKey("projetos", on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.descricao

class status(models.Model):
    status = models.CharField(max_length=10, default = None, null = True)

    def __str__(self):
        return self.status

