"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
	
    # path del admin
    path('admin/', admin.site.urls),

    #path de App Core
    path('', include('Core.urls')),

    #path de App servivios
    path('services/', include('servicios.urls')),

    #path de App blog

    path('blog/',include('blog.urls')),

    #path de App pages

    path('page/',include('pagages.urls')),

    #path de App contactos

    path('contact/',include('contacto.urls')),

    ]
  
# Esto nos permite ver las imagenes desde el admin en modo DEBUG
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)