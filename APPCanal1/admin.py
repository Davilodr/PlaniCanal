from django.contrib import admin

from APPCanal1.models import Avatar, Dias_trabajados, Horas_trabajadas, Personal, PersonalCC, PersonalDXTV

# Register your models here.

admin.site.register(Personal)
admin.site.register(Dias_trabajados)
admin.site.register(Horas_trabajadas)
admin.site.register(PersonalCC)
admin.site.register(PersonalDXTV)
admin.site.register(Avatar)

