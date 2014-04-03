from django.db import models
from django.contrib.auth.models import User

class ItemAgenda(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    usuario = models.ForeignKey(User)
    
