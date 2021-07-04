from django.db import models

# Create your models here.

class Colaborador(models.Model):
    RutColab = models.IntegerField(primary_key=True, verbose_name='Rut Colaborador')
    Fotografia = models.ImageField(upload_to='img/',null=True,blank=True)
    Nombre = models.CharField(max_length=70, verbose_name='Nombre del Colaborador')
    Fono = models.IntegerField(verbose_name='Numbero de Telefono')
    Direcc = models.CharField(max_length=30, verbose_name='Direccion')
    Email = models.CharField(max_length=70, verbose_name='Correo del colaborador')
    Pais = models.CharField(max_length=70, verbose_name='Pais')
    Contra = models.CharField(max_length=15, verbose_name='Contraseña')

    def __int__(self):
        return (self.RutColab)