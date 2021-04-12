from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name="buscar"),
    path('aniadir', views.aniadir, name="aniadir"),
    path('info/<str:id>', views.info, name="info"),
    path('editar/<str:id>', views.editar, name="editar"),
    path('eliminar/<str:id>', views.eliminar, name="eliminar"),
]