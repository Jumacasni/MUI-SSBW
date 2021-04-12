from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField
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

comentarios = [
	{
		'contenido': 'Primer comentario',
		'autor': 'Yo'
	}
]

excursion = Excursion(nombre="Primera excursión", descripcion="Esta es una excursión de prueba", likes=1, 
                      tags=['fácil'], comentarios=comentarios, fotos=[
										                      {'pie':'foto1', 'file':"foto1.jpg"},
										                      {'pie':'foto2', 'file':"foto2.jpg"}
										                      ])
excursion.save() # Para escribir en la BD

...

for excursion in Excursion.objects():
	print(excursion.nombre)