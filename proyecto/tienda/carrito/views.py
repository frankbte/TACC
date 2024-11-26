from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from users.models import Producto


@login_required
def obtener_cantidad_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    cantidad = sum(item.cantidad for item in carrito.items.all())  # Total de productos en el carrito
    return cantidad

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not creado:
        item.cantidad += 1
        item.save()

    return redirect('productos')
@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.subtotal() for item in items)
    return render(request, 'carrito/carrito.html', {'items': items, 'total': total})

@login_required
def eliminar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    item = get_object_or_404(ItemCarrito, carrito=carrito, producto_id=producto_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def actualizar_carrito(request, producto_id):
    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        carrito = get_object_or_404(Carrito, usuario=request.user)
        item = get_object_or_404(ItemCarrito, carrito=carrito, producto_id=producto_id)
        if nueva_cantidad > 0:
            item.cantidad = nueva_cantidad
            item.save()
        else:
            item.delete()
    return redirect('ver_carrito')


