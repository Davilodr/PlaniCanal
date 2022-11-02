
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Dias_trabajados, Personal
from django.views.generic import ListView

def Index(request):
    return render(request, "index.html")

def Crear_Datos(request):
    return render(request, "Crear_Datos.html")

def Buscar_datos(request):
    return render(request, "Buscar_datos.html")

def Buscar_dias(request):
    return render(request, "Buscar_dias.html")

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



def Buscar_dias(request):
    pass
    

class DiasList(ListView):
    model = Dias_trabajados
    template_name = 'Lista_dias.html'
    context_object_name = "ListaDias"


class Crear_dias(CreateView):
    model = Dias_trabajados
    template_name = "Crear_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'


class Ver_dias(DetailView):
    model = Dias_trabajados
    template_name = "Ver_dias.html"
    context_object_name = "VerD"

class Update_dias(UpdateView):
    model = Dias_trabajados
    template_name = "Actualizar_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'
    
    
class Borrar_dias(DeleteView):
    model = Dias_trabajados
    template_name = "Borrar_dias.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_dias/'

class Lista_personal(ListView):
    model = Personal
    template_name = "Lista_Personal.html"
    context_object_name = "ListaPers"
    
class Crear_Personal(CreateView):
    model = Personal
    template_name = "Crear_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'

class Update_Personal(UpdateView):
    model = Personal
    template_name = "Actualizar_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'

class Borrar_Personal(DeleteView):
    model = Personal
    template_name = "Borrar_Personal.html"
    fields =('__all__')
    success_url = '/APPCanal1/Lista_Personal/'




