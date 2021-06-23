from django.db import models    #importamos tablas de la bd
from django.utils import timezone   #importamos función fecha-hora
from django.contrib.auth.models import User #importamos user

# Create your models here.

class portfolio(models.Model):    #creamos la clase Anuncios
    STATUS_CHOICES = (          #definimos los estados
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=150, verbose_name='Título')
    texto = models.TextField(verbose_name='Contenido')
    autor = models.CharField(max_length=150, null=False, verbose_name='miloud')
    image = models.ImageField(null = True, upload_to='portfolio', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última Edición')
    estado = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='borrador')

    class Meta:                  #Creamos la clase metadatos
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering = ('-created',) #Odena por fechas
    def __str__(self):    #Función que devuelve el titulo
        return self.titulo

