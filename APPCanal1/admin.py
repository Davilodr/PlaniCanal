from django.contrib import admin

from APPCanal1.models import Dias_trabajados, Horas_trabajadas, Personal

# Register your models here.

admin.site.register(Personal)
admin.site.register(Dias_trabajados)
admin.site.register(Horas_trabajadas)