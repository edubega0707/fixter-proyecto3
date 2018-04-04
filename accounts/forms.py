from  django import forms
from  django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields='__all__'
        exclude=['user']


class  UserCreateForm(forms.ModelForm):
    password    = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2   = forms.CharField(label='Repite contraseña', widget=forms.PasswordInput())
    username    = forms.CharField(label='Nombre de usuario', widget=forms.TextInput())
    email       = forms.EmailField(label='Correo', widget=forms.EmailInput())
    
    
    class Meta:
        model=User
        fields=['username', 'email']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            return cd['password2']
    

