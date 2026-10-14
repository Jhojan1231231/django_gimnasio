from django.db import models

class plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.IntegerField(help_text="Duración en meses")

    def __str__(self):
        return self.nombre
    
class socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    plan = models.ForeignKey(plan, on_delete=models.CASCADE)
    mensualidad = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

