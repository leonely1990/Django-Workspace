from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    nombres_usuario = models.CharField(
        verbose_name="Nombres",
        max_length=255,
        blank=False,
        null=False
    )
    
    apellidos_usuario = models.CharField(
        verbose_name="Apellidos",
        max_length=255,
        blank=False,
        null=False
    )
    
    fecha_nacimiento = models.DateField(
        verbose_name="F_Nacimiento",
        null=False,
        blank=False
    )
    
    correo_e = models.EmailField(
        verbose_name="Correo_E",
        null=False,
        blank=False,
        unique=True
    )
    
    GENERO = (
        ('M','Masculino'),
        ('F','Femenino')
    )
    
    genero_usuario = models.CharField(
        verbose_name="Genero",
        choices=GENERO,
        default='M',
        max_length=1
    )
    
    fecha_registro = models.DateTimeField(
        verbose_name="Fecha_R",
        auto_now_add=True,
        blank=False,
        null=False
    )
    
    foto = models.ImageField(
        upload_to='fotos/%Y/%m/%d/'
    )
    
    def __str__(self) -> str:
        return self.correo_e