from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.buscar, name="buscar"),
    path('aniadir', views.aniadir, name="aniadir"),
    path('info/<str:id>', views.info, name="info"),
    path('editar/<str:id>', views.editar, name="editar"),
    path('eliminar/<str:id>', views.eliminar, name="eliminar"),
    path('registrar', views.registrar, name="registrar"),
    path('api/excursion/<id>', views.ExcursionView.as_view(), name="excursion"),
    path('api/excursiones', views.ExcursionesView.as_view(), name="excursiones"),
    path('likes/<id>', views.cambiarLikes, name="cambiarLikes")
]