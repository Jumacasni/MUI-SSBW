from django.shortcuts import render
from .models import Excursion

# Create your views here.
def excursion_list(request):
	excursiones = Excursion.objects.all()
	return render(request, 'senderos/excursiones.html', {'excursiones': excursiones})

def buscar(request):
	busqueda = request.POST.get('busqueda','')
	print(busqueda)
	context = {
		'buscado': busqueda,
		'excursiones': Excursion.objects.all()
	}
	
	return render(request, 'senderos/index.html', context)