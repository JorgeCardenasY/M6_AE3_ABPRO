from django.shortcuts import render
from .models import Receta

def index(request):
    return render(request, 'index.html')

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})

def contacto(request):
    return render(request, 'contacto.html')

def detalle_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    return render(request, 'detalle_receta.html', {'receta': receta})

def about(request):
    return render(request, 'about.html')
