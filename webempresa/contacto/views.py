from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import contactForm
from django.core.mail import EmailMessage

# Create your views here.
def Contacto(request):	
	#creamos una instancia del formulario y pasamos como contexto por un diccionario

	formulario = contactForm()
	if request.method == 'POST':
		formulario = contactForm(data=request.POST) # rellena los campos del formulario
		if formulario.is_valid():
			nombre = request.POST.get('nombre','')
			email = request.POST.get('email','')
			contenido = request.POST.get('contenido','')
			# enviamos el correo con los datos
			email = EmailMessage(
				'La Cafeteria: Nuevo mensaje de contacto',
				'De: {} <{}>\n\n Escribio:\n\n {}'.format(nombre,email,contenido),
				'no-contestar@inbox.mailtrap.io',
				# lista de correos donde queremos que nos llegue el mensjae
				['devrandy21@gmail.com'],
				reply_to=[email]
				)
			try:
				email.send()
				return redirect(reverse('contacto')+'?ok')
			except:
				return redirect(reverse('contacto')+'?fail')

	return render(request,"contacto/contacto.html",{'formulario':formulario})