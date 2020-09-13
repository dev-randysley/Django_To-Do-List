from django.shortcuts import render
from .models import Thread
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404

# Create your views here.
@method_decorator(login_required,name='dispatch')
class ThreadListView(TemplateView):
	template_name = 'messenger/thread_list.html'

@method_decorator(login_required,name='dispatch')
class ThreadDetailView(DetailView):
	model = Thread

	def get_object(self):
		# recuperamos el objeto actual por medio del perfil de usuario utilizando la super clase
		obj = super(ThreadDetailView,self).get_object()

		#Comprobamos  si el usuario pertecene al hilo

		if self.request.user not in obj.users.all():
			# si el usuario no pertenece al hilo, no podemos dejar que vea los mensajes
			raise Http404() # lanzamos un error generico

		return obj