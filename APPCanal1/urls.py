   

from django.urls import path


from .views import (
Borrar_Personal,
Borrar_dias, 
Buscar_datos, 
Buscar_dias, 
Buscar_personal, 
BuscarP, 
Crear_Datos, 
Crear_Hora, 
Crear_Personal, 
Crear_dias, 
DiasList, 
HorasList, 
Index, 
Lista_personal, 
Update_Personal, 
Update_dias, 
Ver_dias,
loginview,
rigistrarse,
)

from django.contrib.auth.views import LogoutView


urlpatterns =[
    path('', Index, name="index"), 
    path('Lista_dias/', DiasList.as_view(), name="ListaDias"),  
    path('Ver_Dias/<pk>',Ver_dias.as_view(), name="DetalleDias"),
    path('Crear_Dias/', Crear_dias.as_view(), name="CrearDias"),
    path('Actualizar_Dias/<pk>', Update_dias.as_view(), name="UpdateDias"),
    path('Eliminar_Dias/<pk>', Borrar_dias.as_view(), name="BorrarDias"),
    path('Crear_Personal', Crear_Personal.as_view(), name="CreaPersonal"),
    path('Lista_Personal/', Lista_personal.as_view(), name="ListaPersonal"),
    path('Actualizar_Personal/<pk>', Update_Personal.as_view(), name="UpdatePersonal"),
    path('Eliminar_Personal/<pk>', Borrar_Personal.as_view(), name="BorrarPersonal"),
    path('Crear_Horas/', Crear_Hora.as_view(), name="CrearHoras"),
    path('Lista_Horas/', HorasList.as_view(), name="ListaHoras"),
    path('Crear_Datos', Crear_Datos, name="CrearDatos"),
    path('Buscar_Datos', Buscar_datos, name="BuscarDatos"),
    path('Buscar_dias', Buscar_dias, name="BuscarDias"),
    path('Buscar_Personal', Buscar_personal, name="BuscarPersonal"),
    path('BuscarP', BuscarP, name="BuscarP"),
    path('Login', loginview, name="login"),
    path('Registrarse', rigistrarse, name="Registrar"),
    path('Logout', LogoutView.as_view(template_name="logout.html"), name="logout"),
   

]