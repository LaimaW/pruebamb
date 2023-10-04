from django.shortcuts import render

# Create your views here.

def car(request):
    return render(request, "core/ver_carrito.html")

