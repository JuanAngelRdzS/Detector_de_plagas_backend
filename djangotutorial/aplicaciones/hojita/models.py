from django.db import models

class Registro(models.Model):
    IdUser = models.CharField(max_length=100, primary_key=True)
    NameUser = models.CharField(max_length=100)
    CorreoUse = models.EmailField()
    PassUser = models.CharField(max_length=128, default="default_password")
    telefonoUser = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        # Representación para facilitar la visualización en el CRUD
        return f"Usuario: {self.NameUser} | Correo: {self.CorreoUse} | Teléfono: {self.telefonoUser or 'N/A'}"


class Plaga(models.Model):
    IdPlaga = models.CharField(max_length=100, primary_key=True)
    NamePlaga = models.CharField(max_length=100)
    DescPlaga = models.TextField()
    FotoPlaga = models.ImageField(upload_to='plagas/', blank=True, null=True)

    def __str__(self):
        # Representación para visualizar nombre y descripción
        return f"Plaga: {self.NamePlaga} | Descripción: {self.DescPlaga[:50]}{'...' if len(self.DescPlaga) > 50 else ''}"


class Historial(models.Model):
    Registro = models.ForeignKey(Registro, on_delete=models.CASCADE)  # Relación con Usuario
    Plaga = models.ForeignKey(Plaga, on_delete=models.CASCADE)  # Relación con Plaga
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Representación para visualizar el historial
        return f"Historial: Usuario({self.Registro.NameUser}) - Plaga({self.Plaga.NamePlaga}) | Fecha: {self.fecha_hora}"
