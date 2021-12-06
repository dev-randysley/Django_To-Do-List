from .forms import FormWithEmail, ProfileForm, EmailForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile

# Create your views here.

# Signup = registro
# Utilizamos CreateView cada para crear una instancia nueva que va a nuestra BBDDs
class SignUpView(CreateView):
	form_class = FormWithEmail
	template_name='registration/signup.html'
	def get_success_url(self):
		return reverse_lazy('login') + '?register'

	def get_form(self):
		formu = super(SignUpView,self).get_form()
		# modifico el formulario en tiempo real

		formu.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre usuario'})
		formu.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Email usuario'})
		formu.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
		formu.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repite la Contraseña'})

		# para modificar las etiquetas
		"""formu.fields['username'].label=''
		formu.fields['password1'].label=''
		formu.fields['password2'].label=''"""
		return formu

# debido a que no debe tener acceso al perfil alguien que no este logiado, colocamos un decorador de acceso

@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
	form_class = ProfileForm
	success_url=reverse_lazy('profile')
	template_name ='registration/profile_form.html'

	# para obtener datos del usuario y poder saber que perfil queremos pasar a la UpdateView

	def get_object(self):
		# recupero el objeto que se va a editar

		(profile,created) = Profile.objects.get_or_create(user=self.request.user)

		return profile

@method_decorator(login_required,name='dispatch')
class EmailUpdate(UpdateView):
	form_class = EmailForm
	success_url=reverse_lazy('profile')
	template_name ='registration/profile_email_form.html'

	# para obtener datos del usuario y poder saber que perfil queremos pasar a la UpdateView

	def get_object(self):
		# recupero el objeto que se va a editar
		return self.request.user

	def get_form(self):
		form = super(EmailUpdate,self).get_form()
		form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'New Email'})
		return form