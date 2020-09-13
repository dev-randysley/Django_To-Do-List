from django.contrib import admin
from .models import Categoria,post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
	readonly_fields=('created','update')

class PostAdmin(admin.ModelAdmin):
	readonly_fields=('created','update')
	list_display=('titulo','autor','mostrar_categoria')
	ordering=('titulo',)
	search_fields=('titulo','autor__username','categoria__nombre')
	date_hierarchy='publicacion'
	list_filter=('categoria__nombre',)

	def mostrar_categoria(self,obj):
		return ', '.join([c.nombre for c in obj.categoria.all().order_by('nombre')])
	mostrar_categoria.short_description="Categorias"

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(post,PostAdmin)