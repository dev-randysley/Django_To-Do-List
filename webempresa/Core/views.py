from django.shortcuts import render

# Create your views here.
def Inicio(request):
	return render(request,"Core/portada.html")

def Historia(request):
	return render(request,"Core/historia.html")

def Visitanos(request):
	return render(request,"Core/visitanos.html")

def Blog(request):
	return render(request,"Core/blog.html")

