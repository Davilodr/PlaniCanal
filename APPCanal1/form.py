from django import forms


class Dias_Formulario(forms.Form):

    dni = forms.IntegerField()
    dia_trabajado = forms.DateField()
