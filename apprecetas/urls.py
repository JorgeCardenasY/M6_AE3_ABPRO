from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/', views.recetas, name='recetas'),
    path('contacto/', views.contacto, name='contacto'),
]