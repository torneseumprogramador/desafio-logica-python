from django.db import models

# Create your models here.
class Contato(models.Model):
    class Meta:
        db_table = 'web_contatos'

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=50)