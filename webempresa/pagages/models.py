from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class pages(models.Model):
	title = models.CharField(max_length=200,verbose_name='Titulo')
	Content = RichTextField(verbose_name='Contenido')
	order = models.SmallIntegerField(verbose_name='orden',default=0)
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
	update = models.DateTimeField(auto_now=True,verbose_name='Ultima Actualizacion')

	class Meta:
		verbose_name ='pagina'
		verbose_name_plural ='Paginas'
		ordering = ['order','title']

	def __str__(self):
		return self.title