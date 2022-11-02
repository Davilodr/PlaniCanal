   

from django.urls import path


from .views import (Borrar_Personal,
Borrar_dias, Buscar_datos, Buscar_dias, Buscar_personal, BuscarP, Crear_Datos, 
Crear_Personal, 
Crear_dias, DiasList, 
Index, Lista_personal, 
Update_Personal, 
Update_dias, 
Ver_dias,
)


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
    path('Crear_Datos', Crear_Datos, name="CrearDatos"),
    path('Buscar_Datos', Buscar_datos, name="BuscarDatos"),
    path('Buscar_dias', Buscar_dias, name="BuscarDias"),
    path('Buscar_Personal', Buscar_personal, name="BuscarPersonal"),
    path('BuscarP', BuscarP, name="BuscarP"),
   

]