from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
# Create your models here.

class Messange(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	# si se borra el user de la base de datos tambien se borran todos los mensajes que tiene 
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['created']
		verbose_name ='Mensaje'
		verbose_name_plural='Mensajes'


class ThreadManager(models.Manager):
	
	def find(self,user1,user2):

		query_set= self.filter(users=user1).filter(users=user2)

		if len(query_set) > 0:
			return query_set[0]
		else:
			return None
	def find_or_create(self,user1,user2):

		thread=self.find(user1,user2)

		if thread:
			return thread
		else:
			thread = Thread.objects.create()
			thread.users.add(user1,user2)


class Thread(models.Model):

	# Agregamos un nombre relativo para poder acceder a user de forma inversa
	users = models.ManyToManyField(User,related_name='threads')
	# related_name es el nombre de la relacion inversa entre User y el modelo Thread para acceder a el
	# de esta forma tendremos las instancias del usuario que tengan un Thread
	# de esta forma podremos hacer user.thread para ver los hilos a los que pertenece el usuario
	messages = models.ManyToManyField(Messange)

	objects = ThreadManager()

	class Meta:
		verbose_name ='Hilo de conversacion'
		verbose_name_plural='Hilos de conversacion'


def message_changed(sender,**kwargs):
	instance = kwargs.pop('instance',None)
	action = kwargs.pop('action',None)
	pk_set = kwargs.pop('pk_set',None)


	set_pk_message_false = set()
	if action is "pre_add":
		for msj_pk in pk_set:
			#rescato el mensaj con la llave primaria
			msg = Messange.objects.get(pk=msj_pk)
			if msg.user not in instance.users.all():
				set_pk_message_false.add(msj_pk)
		pk_set.difference_update(set_pk_message_false)



m2m_changed.connect(message_changed,sender=Thread.messages.through)