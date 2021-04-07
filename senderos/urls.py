from django.urls import path
from . import views

urlpatterns = [
    path('', views.excursion_list, name='excursion_list'),
    path('buscar', views.buscar, name="buscar"),
]