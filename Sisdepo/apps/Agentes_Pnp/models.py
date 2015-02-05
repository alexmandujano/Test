from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save,post_init,pre_save,post_delete
import os
from django.conf import settings
from apps.Comisaria.models import Comisaria
class Agente(models.Model):
	COD_POLICIA=models.CharField(_('Codigo Policial'), max_length=50,unique=True)
	NOM_POLICIA=models.CharField(_('Nombres'), max_length=50)
	APELLIDO_P=models.CharField(_('Apellido P'), max_length=20)
	APELLIDO_M=models.CharField(_('Apellido M'), max_length=20)
	DNI=models.CharField(max_length=8)
	COMISARIA=models.ForeignKey(Comisaria)
	CARGO=models.CharField(max_length=8)		
	USUARIO=models.OneToOneField(User,null=True)
	FOTO=models.ImageField(upload_to='foto_agente')
	CONFORME=models.BooleanField(default=False,editable=True)

	def __unicode__(self):

		return self.CARGO+' '+self.APELLIDO_M+' '+self.APELLIDO_M+' '+self.NOM_POLICIA 
	
	def traer_url_foto(self):
		
		return 'http://127.0.0.1:8000/media/%s' % self.FOTO


Fotoactual = {}
@receiver(pre_save,sender=Agente,dispatch_uid="pre_save_foto")
def CogerFotoActual(sender, instance, **Kwargs):
	try:
		agente=(Agente.objects.get(pk=instance.pk))  #este codigo funcionara solo si ya existe una imagen asociada al agente
		Fotoactual[instance.id]=agente.FOTO          #de no existir quiere decir que se esta agregado un nuevo agente por lo que no existe imagen guardada aun
	except:
		Fotoactual.clear()
		pass										 

@receiver(post_save,sender=Agente,dispatch_uid="post_save_foto")
def ComprobarFoto(sender, instance, created, **Kwargs):
	
	if created:                             #Si se esta creando u nuevo usuario seguira su camnino
		pass
	else:									#si el usuario no se esta creando quiere decir que se actualizara 
		FotoGuardada=str(instance.FOTO)
		FotoInicial=str(Fotoactual[instance.id])
		if FotoGuardada != FotoInicial :	#para lo cual comprobaremos si se trata de una foto nueva y asi poder eliminar la foto antigua
			try:
				os.remove(os.path.join(settings.MEDIA_ROOT,FotoInicial)) #elimina la foto inicial devido a que ya a sido cambiada
				Fotoactual.clear()
			except:
				Fotoactual.clear()
				pass

@receiver(post_delete,sender=Agente, dispatch_uid='post_delete_Foto')
def EliminarFoto(sender, instance, **Kwargs):
	instance.FOTO.delete(False)  #esto elimina la foto relacionada al agente de la base y de la ruta


	

		

	





