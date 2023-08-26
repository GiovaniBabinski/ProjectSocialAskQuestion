from django.db import models
from django.conf import settings

class Pergunta(models.Model):
    publicado = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



class Resposta(models.Model):
    publicado = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor.username
