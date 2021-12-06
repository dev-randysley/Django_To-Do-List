from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=100,verbose_name='Nombre')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
	update = models.DateTimeField(auto_now=True,verbose_name='Ultima Actualizacion')

	class Meta:
		verbose_name ='Categoria'
		verbose_name_plural ='Categorias'
		ordering = ['-created']

	def __str__(self):
		return self.nombre

class post(models.Model):
	titulo = models.CharField(max_length=200,verbose_name='Titulo')
	descripcion=models.TextField(verbose_name='Contenido')
	publicacion = models.DateTimeField(verbose_name='Fecha de publicacion',default=now)
	imagen=models.ImageField(verbose_name='Imagen',upload_to='blog',null=True,blank=True)
	#Uso de relaciones
	autor=models.ForeignKey(User,verbose_name='Autor',on_delete=models.CASCADE)
	categoria = models.ManyToManyField(Categoria,verbose_name='Categorias',related_name='Obtener_publicaciones')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
	update = models.DateTimeField(auto_now=True,verbose_name='Ultima Actualizacion')

	class Meta:
		verbose_name ='Publicacion'
		verbose_name_plural ='Publicaciones'
		ordering = ['-created']

	def __str__(self):
		return self.titulo