from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance,filename):
	# obtengo la instancia anterior qu tenga el id pk
	old_instance = Profile.objects.get(pk=instance.pk)
	#elimino la imagen anterior
	old_instance.avatar.delete()

	return 'profiles/'+filename


# Create your models here.
class Profile(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Usuario')
	avatar = models.ImageField(upload_to=custom_upload_to,blank=True,null=True)
	bio = models.TextField(blank=True,null=True)
	link=models.URLField(max_length=200,blank=True,null=True)

	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"
		ordering = ['user']
	def __str__(self):
		return self.user

	# Ahora debemos crear la relacion de este modelo con el modelo User que nos gestion Django

@receiver(post_save,sender=User)
def ensure_profile_exists(sender,instance,**kwargs):
	if kwargs.get('created',False):
		Profile.objects.get_or_create(user=instance)
		
