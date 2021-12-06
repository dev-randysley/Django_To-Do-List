from django.db import models

# Create your models here.
class Link(models.Model):
	key = models.SlugField(verbose_name='Nombre clave',unique=True,max_length=100)
	name = models.CharField(max_length=200,verbose_name='Red Social')
	url = models.URLField(blank=True,null=True,verbose_name='enlace',max_length=200)
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
	update = models.DateTimeField(auto_now=True,verbose_name='Ultima Actualizacion')

	class Meta:
		verbose_name ='Enlace'
		verbose_name_plural ='Enlaces'
		ordering = ['-name']

	def __str__(self):
		return self.name