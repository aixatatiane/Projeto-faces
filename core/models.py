from django.db import models
from django.contrib.auth.models import User

class Faces(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ocupacao = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    data_falecimento = models.DateField()
    imagem = models.ImageField(upload_to='uploads/%y%y%y%y/%m%m/%d%d')
    postado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome