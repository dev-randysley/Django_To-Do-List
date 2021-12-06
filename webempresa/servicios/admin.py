from django.contrib import admin

from .models import servicios

# Register your models here
class AdminServicios(admin.ModelAdmin):
	readonly_fields = ('created','update')

admin.site.register(servicios,AdminServicios)

