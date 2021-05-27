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

class FotosSerializer(serializers.Serializer):
	file = serializers.CharField(required=False)
	pie = serializers.CharField(required=False, max_length=120)

class ComentariosSerializer(serializers.Serializer):
	contenido = serializers.CharField(required=True)
	autor     = serializers.CharField(max_length=120, required=True)
	fecha     = serializers.DateTimeField(default=datetime.now())

class ExcursionSerializer(serializers.Serializer):
	id 					= serializers.UUIDField(required=False)
	nombre 			= serializers.CharField(required=False,max_length=120)
	descripcion = serializers.CharField(required=False,validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")])
	likes 			= serializers.CharField(default=0)
	fotos 			= FotosSerializer(required=False, many=True)

	def create(self, validated_data):
		excursion = Excursion(nombre = validated_data['nombre'], descripcion=validated_data['descripcion']).save()

		if validated_data.get('file', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.fotos.append(Fotos(pie=validated_data['pie'], file=validated_data['file']))
			else:
				excursion.fotos.append(Fotos(file=validated_data['file'], pie=None))

		return excursion

	def update(self, excursion, validated_data):
		if validated_data.get('nombre') is not None:
			excursion.nombre = validated_data['nombre']

		if validated_data.get('descripcion') is not None:
			excursion.descripcion = validated_data['descripcion']

		if validated_data.get('likes') is not None:
			excursion.likes = validated_data['likes']
		
		if validated_data.get('file', None) is not None:
			if validated_data.get('pie', None) is not None:
				excursion.fotos.append(Fotos(pie=validated_data['pie'], file=validated_data['file']))
			else:
				excursion.fotos.append(Fotos(file=validated_data['foto'], pie=None))
			
		excursion.save()
		return excursion
