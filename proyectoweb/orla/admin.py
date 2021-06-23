from django.contrib import admin

# Register your models here.
from .models import Curso
from .models import Orla

# vamos a crear las clases para administrar los cursos (objetos Curso) y los objetos Orla (orlas)
"""
aqui vamos crear una clase que herede de la clase admin.ModelAdmin que nos permite hacer 
modificaciones en los models que estamos trabajando en el pad. UNa vez creada le
digo que campos quiero que se vean en el pad para (el modelo) Curso y Orla
...eso lo hacemos usando un método llamado "list_display" ..
 TB ME INTEREA UN CAMPO DE BUSQUEDA PARA PODER SELECCIONAR REGISTROS FILTRAOS (SELECT WHERE)
 SI EL NUMERO DE CURSOS Y ALUMNOS FUERA MUY GRANDE

Añado un filtro para poder filtrar en OrlaAdmin, los profesores de los alumnos y otro en 
Curso para poder filtrar los cursos por fecha
ADEMAS CUANDO TRABAJAMOS CON FECHAS PODEMOS INTRODUCIR UN FILTRO
tipo un menu de tipo horizontal que nos va indicando lo que vamos filtrando


"""



class CursoAdmin(admin.ModelAdmin):
    list_display=("num","titulo", "subtitulo", "Fecha", "logo")
    search_fields=("num","titulo", "Fecha")
    list_filter=("Fecha",)
    DateField="Fecha"

class OrlaAdmin(admin.ModelAdmin):
    list_display=("propietario","nombre", "apellidos", "texto", "image", "video", "created", "estado")
    search_fields=("propietario","nombre", "apellidos")
    list_filter=("estado",)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Orla,OrlaAdmin)