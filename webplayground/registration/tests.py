from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):

	def setUp(self):
		# creamos las instancias que necesitamos para la prueba
		User.objects.create_user('test', 'test@gmail.com', 'test1234')

	def test_existe_perfil(self):
		# codificamos la prueba que queremos que se realice
		exists=Profile.objects.filter(user__username='test').exists()
		# hacemos la comparacion de resultados
		self.assertEqual(exists,True)