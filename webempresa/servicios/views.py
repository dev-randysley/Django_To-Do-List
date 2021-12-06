from django.shortcuts import render

from .models import servicios
# Create your views here.

def Servicios(request):
	# cargamos todos los registro de nuestra base de datos como objetos y pasamos un diccionario con ellos
	lista_servicios = servicios.objects.all()
	return render(request,"servicios/servicios.html",{'servicios':lista_servicios})