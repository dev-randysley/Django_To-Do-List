from django.shortcuts import render,get_object_or_404

from .models import pages

# Create your views here.
def page(request,pagina_id,pagina_title):
	pagina = get_object_or_404(pages,id=pagina_id)
	return render(request,'pagages/sample.html',{'pagina':pagina})