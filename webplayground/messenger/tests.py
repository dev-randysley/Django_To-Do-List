from django.test import TestCase
from django.contrib.auth.models import User
from .models import Messange, Thread

# Create your tests here.

class MessengeTest(TestCase):

	def setUp(self):
		# creamos las instancias que necesitamos para la prueba
		self.user1=User.objects.create_user('user1', None, 'test1234')
		self.user2=User.objects.create_user('user2', None, 'test1234')
		self.user3=User.objects.create_user('user3', None, 'test1234')

		self.thread = Thread.objects.create()

	def test_Agregando_usuarios_hilo(self):
		# codificamos la prueba que queremos que se realice
		self.thread.users.add(self.user1,self.user2)
		# hacemos la comparacion de resultados
		self.assertEqual(len(self.thread.users.all()),2)

	def test_Filtrar_hilos_por_usuarios(self):

		self.thread.users.add(self.user1,self.user2)

		# Aca estamos filtrando el hilo donde estan ambos usuarios
		hilo=Thread.objects.filter(users=self.user1).filter(users=self.user2)

		self.assertEqual(self.thread,hilo[0])

	def test_Agregar_mensaje_hilo(self):
		self.thread.users.add(self.user1,self.user2)
		Mensaje1 = Messange.objects.create(user=self.user1,content='Muy buenas')
		Mensaje2 = Messange.objects.create(user=self.user2,content='Hola')
		self.thread.messages.add(Mensaje1,Mensaje2)
		self.assertEqual(len(self.thread.messages.all()),2)

		for mensaje in self.thread.messages.all():
			print("({}): {}".format(mensaje.user,mensaje.content))

	def test_Agregando_mensaje_desconocido(self):
		self.thread.users.add(self.user1,self.user2)
		Mensaje1 = Messange.objects.create(user=self.user1,content='Muy buenas')
		Mensaje2 = Messange.objects.create(user=self.user2,content='Hola')
		Mensaje3 = Messange.objects.create(user=self.user3,content='Hola, soy espia')
		self.thread.messages.add(Mensaje1,Mensaje2,Mensaje3)

		self.assertEqual(len(self.thread.messages.all()),2)

	def test_Entonctrar_hilo_custom_manager(self):
		self.thread.users.add(self.user1,self.user2)
		thread = Thread.objects.find(self.user1,self.user2)
		self.assertEqual(self.thread,thread)

	def test_Entonctrar_o_crear_hilo_custom_manager(self):
		self.thread.users.add(self.user1,self.user2)
		thread = Thread.objects.find(self.user1,self.user2)
		self.assertEqual(self.thread,thread)
		thread = Thread.objects.find_or_create(self.user1,self.user2)
		self.assertIsNotNone(thread)