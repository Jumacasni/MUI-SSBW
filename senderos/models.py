from django.db import models

from mongoengine import *
from datetime import datetime

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