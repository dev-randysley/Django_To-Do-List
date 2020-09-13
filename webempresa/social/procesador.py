from .models import Link

def contexto(request):
	links ={}
	enlaces = Link.objects.all()
	for enlace in enlaces:
		links[enlace.key]=enlace.url
	return links

