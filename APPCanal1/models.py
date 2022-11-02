from datetime import datetime
from django.db import models


class Personal(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
    
    

class Dias_trabajados(models.Model):
    
    dni = models.IntegerField()
    dia_trabajado = models.DateField()
    
    
    def __str__(self):
        return f'Dni: {self.dni} - Dia Trabajado: {self.dia_trabajado}'
   

class Horas_trabajados(models.Model):
    
    dni = models.IntegerField()
    hora_trabajado = models.IntegerField()
    Fecha_actual = datetime
    
    def __str__(self):
        return f'{self.dni} - {self.hora_trabajado}'
