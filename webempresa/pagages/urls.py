from django.urls import path

from . import views 

urlpatterns = [
	path('<int:pagina_id>/<slug:pagina_title>',views.page,name='pagina'),
]