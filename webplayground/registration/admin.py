from django.contrib import admin
from .models import Profile
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user',)        


admin.site.register(Profile,RegistrationAdmin)