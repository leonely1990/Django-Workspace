from django.db import models

# Create your models here.

class Categoria(models.Model):
    
    nombre_categoria = models.CharField(
        max_length=50,
        unique=True
    )
    
    descripcion = models.CharField(
        max_length=255,
        blank=True
    )
    
    slug = models.CharField(
        max_length=100,
        blank=True
    )
    
    imagen = models.ImageField(upload_to = 'imagenes/categorias', blank=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self) -> str:
        return self.nombre_categoria