from django.urls import path
from . import views as servicios_views

urlpatterns = [
	path('',servicios_views.Servicios,name='servicios'),
]