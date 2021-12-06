from django import forms

class contactForm(forms.Form):
	nombre=forms.CharField(label='Nombre',required=True,min_length=3,max_length=100,widget=forms.TextInput(
		attrs={'class':'form-control',
				'placeholder':'Escribe tu nombre'}
		))
	email=forms.EmailField(label='Email',required=True,min_length=3,max_length=100,widget=forms.EmailInput(
		attrs={'class':'form-control','placeholder':'Escribe tu email'},
		))
	contenido=forms.CharField(label='Contenido',required=True,min_length=3,max_length=100,widget=forms.Textarea(
		attrs={'class':'form-control',
				'rows':3,
				'placeholder':'Escribe tu mensaje'}
		))

