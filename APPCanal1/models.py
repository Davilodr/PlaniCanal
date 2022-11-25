from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User
from django.db import models



class Personal(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'

class PersonalCC(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares",default='media/avatares/usuario.png', null=True, blank=True, verbose_name="Avatar")
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'

class PersonalDXTV(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares",default='media/avatares/usuario.png', null=True, blank=True, verbose_name="Avatar")
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
    
    

class Dias_trabajados(models.Model):
    
   
    dia_trabajado = models.DateField()
    personal = models.ForeignKey(PersonalCC, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Dia Trabajado: {self.dia_trabajado}'
   

class Horas_trabajadas(models.Model):
    
    
    hora_trabajada = models.IntegerField()
    dia_actual = models.DateField(auto_now_add=True)
    personal1 = models.ForeignKey(PersonalDXTV, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'{self.dia_actual} - {self.hora_trabajada}'
    
class Supervisor(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
    
    
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    imagen = models.ImageField(upload_to="avatares",default='default.png', null=True, blank=True, verbose_name="Avatar")
    
    def __str__(self):
        return f'{self.user} - {self.imagen}'
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')
    
    

    
    
    
    
    
    

