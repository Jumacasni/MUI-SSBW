from django.shortcuts import render, redirect
from mongoengine.queryset.visitor import Q
from .models import Excursion, Fotos
from .forms import ExcursionForm
from django.contrib import messages
from django.conf import settings
import os
import shutil

IMAGE_DIR = os.path.join(settings.BASE_DIR, 'senderos', 'static', 'img', 'senderos')

def index(request):
	form = ExcursionForm()

	context = {
		'saludo': "buenas tardes",
		'excursiones': Excursion.objects.all()[:4],
		'form': form
	}

	return render(request, 'senderos/index.html', context)

def buscar(request):
	busqueda = request.POST.get('busqueda','')
	context = {
		'buscado': busqueda,
		'excursiones': Excursion.objects(Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda))
	}
	
	return render(request, 'senderos/index.html', context)

def editar(request, id):
	if request.method == 'POST':
		form = ExcursionForm(request.POST, request.FILES)

		if form.is_valid():
			e = Excursion.objects.get(id=id)
			input_d = form.cleaned_data
			files 	= request.FILES

			e.nombre = input_d['nombre']
			e.descripcion = input_d['descripcion']
			e.save()

			if len(files) > 0:
				guardarImagenes(id, files, e, input_d)

			messages.success(request, "Ruta editada con éxito")

		else:
			messages.error(request, "Error en el formulario")

	return redirect('index')

def aniadir(request):
	if request.method == 'POST':
		form = ExcursionForm(request.POST, request.FILES)

		if form.is_valid():
			input_d = form.cleaned_data
			files 	= request.FILES
			reg 		= Excursion(nombre = input_d['nombre'], descripcion=input_d['descripcion']).save()

			if len(files) > 0:
				guardarImagenes(str(reg.id), files, reg, input_d)

			messages.success(request, "Ruta añadida con éxito")

		else:
			messages.error(request, "Error en el formulario")

	return redirect('index')

def guardarImagenes(id, files, e, input_d):
	directorio = os.path.join(IMAGE_DIR, id)

	try:
		if not os.path.exists(directorio):
			os.mkdir(directorio)

		nombre_archivo = os.path.join(directorio, str(files['foto']))
		with open(nombre_archivo, 'wb+') as dest:
			for chunk in files['foto'].chunks():
				dest.write(chunk)

		if len(e.fotos) == 0:
			e.fotos=[Fotos(pie=input_d.get('pie'), file=input_d.get('foto').name)]
		else:
			e.fotos.append(Fotos(pie=input_d.get('pie'), file=input_d.get('foto').name))

		e.save()

	except OSError as error:
		print('**************** ERROR', error)

def info(request, id):
	form = ExcursionForm()

	context={
		'id_excursion': Excursion.objects(id=id)[0].id,
		'nombre': Excursion.objects(id=id)[0].nombre,
		'descripcion': Excursion.objects(id=id)[0].descripcion,
		'fotos': Excursion.objects(id=id)[0].fotos,
		'n_fotos': len(Excursion.objects(id=id)[0].fotos),
		'comentarios': Excursion.objects(id=id)[0].comentarios,
		'form': form
	}
	
	return render(request, 'senderos/info.html', context)

def eliminar(request, id):
	directorio = os.path.join(IMAGE_DIR, id)

	shutil.rmtree(directorio)

	Excursion.objects(id=id).delete()
	
	return redirect('index')