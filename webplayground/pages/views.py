from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .models import Page

# Create your views here.
"""class PermitirAcceso(object):

	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(PermitirAcceso,self).dispatch(request,*args,**kwargs)"""

# clases para leer la informacion READ
class PagesListView(ListView):

 	model = Page

class PageDetailView(DetailView):
    
    model =Page

# clase para crear CREATE
# Agregamos un decorador para el acceso a estas vistas
@method_decorator(staff_member_required,name='dispatch')
class PageCreate(CreateView):
	model= Page
	fields=['title','content','order']
	success_url = reverse_lazy('pages:pages')


#Clase para actualizar UPDATE
@method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
	model = Page
	fields = ['title','content','order']
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse_lazy('pages:update',args=[self.object.id]) +'?ok'

#Clase para eliminar DELETE
@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
	model=Page
	success_url=reverse_lazy('pages:pages')
	template_name='pages/eliminar_pagina.html'