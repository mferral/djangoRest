from django.db import models

# Create your models here.
class Cliente(models.Model):        
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    foto = models.ImageField(upload_to = 'fotos/', blank=True, null=True)
    archivo = models.FileField(upload_to = 'archivo/', blank=True, null=True)

    def get_nombre_completo(self):  
        return self.nombre + ' ' + self.apellido