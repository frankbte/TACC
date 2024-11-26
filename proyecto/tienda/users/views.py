from django.shortcuts import render, HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Profile
from .models import Producto
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def productos(request):
    productos = Producto.objects.all()
    data  = {'productos': productos}
    return render(request, 'users/productos.html', data)

def contact(request):
    return render(request, 'users/contact.html')

def about(request):
    return render(request, 'users/about.html')

def regsitro (request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return redirect("home")

