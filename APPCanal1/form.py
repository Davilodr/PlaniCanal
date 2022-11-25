from django import forms

from APPCanal1.models import Avatar, Dias_trabajados
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class Dias_Formulario(forms.ModelForm):

    class Meta:
        model = Dias_trabajados
        fields = ('__all__')
        widgets ={
            'dia_trabajado': forms.TextInput(
                attrs={
                    'placeholder': "año/mes/dia",
                }
            )
        }

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    

    class Meta:

        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
        
    
class PersonalFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    email = forms.EmailField(max_length=254)
    
    
class AvatarForm(forms.ModelForm):
        
    class Meta:
        model = Avatar
        fields = ['imagen']
        