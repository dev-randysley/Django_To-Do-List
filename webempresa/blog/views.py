from django.shortcuts import render, get_object_or_404
from .models import post,Categoria

# Create your views here.

def blog(request):
	publicaciones = post.objects.all()
	return render(request,'blog/blog.html',{'posts':publicaciones})

def categoria(request,categoria_id):
	categoria = get_object_or_404(Categoria,id=categoria_id)
	return render(request,'blog/categoria.html',{'categoria':categoria})
	