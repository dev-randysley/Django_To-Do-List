from django.contrib import admin

from .models import pages

# Register your models here.
class pagesAdmin(admin.ModelAdmin):
	readonly_fields=('created','update')
	list_display=('title','order')

admin.site.register(pages,pagesAdmin)