from django.db import models

from mongoengine import *
from datetime import datetime
from rest_framework import serializers
from django.core.validators import RegexValidator, FileExtensionValidator
# from rest_framework_mongoengine import serializers

connect('senderos', host='mongo')

class Comentarios(EmbeddedDocument):
	contenido = StringField(required=True)
	autor     = StringField(max_length=120, required=True)
	fecha     = DateTimeField(default=datetime.now())

class Fotos(EmbeddedDocument):
	pie = StringField(required=False, max_length=120)
	file = StringField(required=False)

class Excursion(Document):
	nombre      = StringField(max_length=120, required=True)
	descripcion = StringField(required=True)
	likes       = IntField(default=0)
	visitas     = IntField(default=0)
	tags        = ListField(StringField(max_length=20))
	duracion    = IntField(default=0)
	comentarios = ListField(EmbeddedDocumentField(Comentarios))
	fotos	      = ListField(EmbeddedDocumentField(Fotos))

class ExcursionSerializer(serializers.Serializer):
	nombre 			= serializers.CharField(max_length=120)
	descripcion = serializers.CharField(validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")])
	foto 				= serializers.FileField(required=False, validators=[FileExtensionValidator(
																										allowed_extensions=['jpg', 'jpeg', 'png'])])
	pie 				= serializers.CharField(max_length=80, required=False)

	def create(self, validated_data):
		excursion = Excursion(nombre = validated_data['nombre'], descripcion=validated_data['descripcion']).save()

		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.fotos.append(Fotos(pie=validated_data['pie'], foto=validated_data['foto']))
			else:
				excursion.fotos.append(Fotos(foto=validated_data['foto'], pie=None))

		return excursion

	def update(self, excursion, validated_data):
		excursion.nombre = validated_data['nombre']
		excursion.descripcion = validated_data['descripcion']
		
		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.fotos.append(Fotos(pie=validated_data['pie'], foto=validated_data['foto']))
			else:
				excursion.fotos.append(Fotos(foto=validated_data['foto'], pie=None))
			
		excursion.save()
		return excursion
 
# class ExcursionSerializer(serializers.DocumentSerializer):
# 	class Meta:
# 		model: 'Excursion'
# 		fields: ['nombre', 'descripcion']