from django.urls import path
from . import views as Core_views

urlpatterns = [
	
    path('',Core_views.Inicio,name='inicio'),
    path('about/',Core_views.Historia,name='historia'),
    path('visit/',Core_views.Visitanos,name='visitanos'),
    
]
