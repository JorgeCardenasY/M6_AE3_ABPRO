from django.contrib import admin
from .models import Receta
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/', views.recetas, name='apprecetas.views.recetas'),
    path('contacto/', views.contacto, name='contacto'),
]

admin.site.register(Receta)

