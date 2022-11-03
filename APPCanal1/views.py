
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Dias_trabajados, Horas_trabajadas, Personal
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator



def Index(request):
    return render(request, "index.html")
@login_required
def Crear_Datos(request):
    return render(request, "Crear_Datos.html")

@staff_member_required(login_url="/APPCanal1/Login")
def Buscar_datos(request):
    return render(request, "Buscar_datos.html")

@staff_member_required(login_url="/APPCanal1/Login")
def Buscar_dias(request):
    return render(request, "Buscar_dias.html")

@staff_member_required(login_url="/APPCanal1/Login")
def Buscar_personal(request):
    return render(request, "Buscar_personal.html")

def BuscarP(request):
    
    if request.GET["dni"]:

        dni_buscada = request.GET["dni"]

        personal = Personal.objects.get(dni=dni_buscada)

        return render(request, "Resultado_BuscarP.html", {"Personal": personal, "Dni": dni_buscada})

    else:

        respuesta = "No enviaste datos"
        
        return HttpResponse(respuesta)

def BuscarD(request):
    pass

def loginview(request):
    
    if request.method == 'POST':

        Formulariologin = AuthenticationForm(request, data=request.POST)

        if Formulariologin.is_valid():

            data = Formulariologin.cleaned_data
            
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username = usuario, password = psw)
            
            if user:
                
                login(request, user)
                
                return render(request, "index.html")
            else:
                return render(request, "index.html", {"mensaje": f'Error, los datos ingresados son incorrectos'})
        
        return render(request, "index.html",{"mensaje": f'Error, formulario invalido'}) 
    else:

        Formulariologin = AuthenticationForm()

        return render(request, "login.html", {"FormularioLogin": Formulariologin})

def rigistrarse(request):
    
    if request.method == 'POST':

        Formularioregistro = UserCreationForm(request.POST)

        if Formularioregistro.is_valid():

            username = Formularioregistro.cleaned_data["username"]
            
            Formularioregistro.save()
                        
            return render(request, "index.html", {"mensaje": f'Usuario {username} creado con exito'})     
        else:
            return render(request, "index.html",{"mensaje": f'Error, al crear el usuario'})
    else:
        

        Formularioregistro = UserCreationForm()

        return render(request, "registrarse.html", {"FormularioRegistro": Formularioregistro})


    

class DiasList(LoginRequiredMixin, ListView):
    model = Dias_trabajados
    template_name = 'Lista_dias.html'
    context_object_name = "ListaDias"

class Crear_dias(LoginRequiredMixin, CreateView):
    model = Dias_trabajados
    template_name = "Crear_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'

class Ver_dias(LoginRequiredMixin, DetailView):
    model = Dias_trabajados
    template_name = "Ver_dias.html"
    context_object_name = "VerD"

class Update_dias(LoginRequiredMixin, UpdateView):
    model = Dias_trabajados
    template_name = "Actualizar_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'
    
    
class Borrar_dias(LoginRequiredMixin, DeleteView):
    model = Dias_trabajados
    template_name = "Borrar_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'

class Lista_personal(LoginRequiredMixin, ListView):
    model = Personal
    template_name = "Lista_Personal.html"
    context_object_name = "ListaPers"
    
class Crear_Personal(LoginRequiredMixin, CreateView):
    model = Personal
    template_name = "Crear_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'

class Update_Personal(LoginRequiredMixin, UpdateView):
    model = Personal
    template_name = "Actualizar_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'

class Borrar_Personal(LoginRequiredMixin, DeleteView):
    model = Personal
    template_name = "Borrar_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'
    
class HorasList(LoginRequiredMixin,ListView):
    model = Horas_trabajadas
    template_name = 'Lista_Horas.html'
    context_object_name = "ListHoras"


class Crear_Hora(LoginRequiredMixin, CreateView):
    model = Horas_trabajadas
    template_name = "Crear_Hora.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Horas/'


class Ver_Hora(LoginRequiredMixin, DetailView):
    model = Horas_trabajadas
    template_name = "Ver_horas.html"
    context_object_name = "VerH"

class Update_Horas(LoginRequiredMixin, UpdateView):
    model = Horas_trabajadas
    template_name = "Actualizar_Horas.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Horas/'
    
    
class Borrar_Horas(LoginRequiredMixin, DeleteView):
    model = Horas_trabajadas
    template_name = "Borrar_horas.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Horas/'
    

    





