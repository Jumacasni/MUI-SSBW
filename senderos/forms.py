from django import forms
from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExcursionForm(forms.Form):
	nombre 			= forms.CharField(max_length=120)
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":30}),
																validators=[RegexValidator('^[A-Z]', message="No empieza por mayúscula")])
	foto 				= forms.FileField(required=False, validators=[FileExtensionValidator(
																										allowed_extensions=['jpg', 'jpeg', 'png'])])
	pie 				= forms.CharField(max_length=80, required=False)

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]