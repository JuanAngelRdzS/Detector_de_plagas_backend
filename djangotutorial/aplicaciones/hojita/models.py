from django.db import models

# Create your models here.
class Registro(models.Model):
    IdUser = models.CharField(max_length=100, primary_key=True)
    NameUser = models.CharField(max_length=100)
    CorreoUse = models.EmailField()


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.NameUser, self.CorreoUse)