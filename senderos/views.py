from django.shortcuts import render
from .models import Excursion

# Create your views here.
def excursion_list(request):
	excursiones = Excursion.objects.all()
	return render(request, 'senderos/index.html', {'excursiones': excursiones})