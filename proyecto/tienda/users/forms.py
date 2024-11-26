from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User  # Cambia a User, ya que estamos creando un usuario
        fields = ('username', 'password1', 'password2', 'nombre', 'apellido', 'direccion', 'telefono', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)  
        if commit:
            user.save()  

        if not Profile.objects.filter(user=user).exists():
            profile = Profile.objects.create(
                user=user,
                nombre=self.cleaned_data["nombre"],
                apellido=self.cleaned_data["apellido"],
                direccion=self.cleaned_data["direccion"],
                telefono=self.cleaned_data["telefono"],
                email=self.cleaned_data["email"]
            )

        return user
