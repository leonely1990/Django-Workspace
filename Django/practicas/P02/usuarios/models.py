from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    GENERO = (
        ('M','Masculino'),
        ('F', 'Femenino'),
    )
    
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    genero = models.CharField(choices=GENERO, max_length=100)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return "{}".format(self.nombre)