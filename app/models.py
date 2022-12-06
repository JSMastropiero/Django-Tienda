from django.db import models


# Create your models here.

class Marca(models.Model): #El id lo pone automáticamente django.
    nombre = models.CharField(max_length=50) #charfield equivalente a varchar.

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50) 
    precio = models.IntegerField()
    descripcion = models.TextField() 
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices = opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre