from django import template
from pagages.models import pages

register = template.Library()


@register.simple_tag
def Obtener_paginas():
	paginas = list(pages.objects.all())
	return paginas