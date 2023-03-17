from django.db import models

# Create your models here.

class Historia(models.Model):
    nombrePaciente = models.CharField(max_length=50)
    apellidoPaciente = models.CharField(max_length=50)
    edadPaciente = models.IntegerField()
    documento = models.IntegerField()
    fechaNacimiento = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombrePaciente)