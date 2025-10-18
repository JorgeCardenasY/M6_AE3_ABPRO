from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/', views.recetas, name='recetas'),
    path('contacto/', views.contacto, name='contacto'),
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('about/', views.about, name='about'),
]