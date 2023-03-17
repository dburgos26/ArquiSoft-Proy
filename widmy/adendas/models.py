from django.db import models
from historias.models import Historia

# Create your models here.

class Adenda(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    identificador = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return '{}'.format(self.identificador)
