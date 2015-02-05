from django.db import models
from django.db.models.signals import pre_save,post_save,post_delete
import os
from django.conf import settings
from django.dispatch import receiver  

class Denunciado(models.Model):
	COD_DENUNCIADO=models.CharField(max_length=10)
	NOM_DENUNCIADO=models.CharField(max_length=40, blank=True, null=True)
	APELLIDO_P=models.CharField(max_length=20, blank=True, null=True)
	APELLIDO_M=models.CharField(max_length=20, blank=True, null=True)
	EDAD=models.IntegerField(blank=True, null=True)
	DNI=models.CharField(max_length=8, blank=True, null=True)
	SEXO=models.CharField(max_length=1, blank=True, null=True)
	ESTADO_CIV=models.CharField(max_length=1, blank=True, null=True)
	LUG_NAC=models.CharField(max_length=50, blank=True, null=True)
	CARACTERISTICAS=models.TextField(max_length=150, blank=True, null=True)
	OCUPACION=models.CharField(max_length=50, blank=True, null=True)
	DIRECCION=models.CharField(max_length=50)
 
	def __unicode__(self):

		return self.NOM_DENUNCIADO+' '+self.APELLIDO_P+' '+self.APELLIDO_M

	def traer_url_foto(self):

		try:
			FotoDenunciado=Foto_Denunciado.objects.filter(DENUNCIADO=self.pk)[0] #traemos el nombre de la foto que asu vez es una ruta
			return 'http://127.0.0.1:8000/media/%s' % FotoDenunciado.FOTO
		
		except:
			return "No tiene imagen"

class Foto_Denunciado(models.Model):
	DENUNCIADO=models.ForeignKey(Denunciado)
	FOTO=models.ImageField(upload_to='foto_denunciado')
 
	def __unicode__(self):
		return self.DENUNCIADO.NOM_DENUNCIADO 





Fotoactual = {} #definimos un diccionario de datos
@receiver(pre_save,sender=Foto_Denunciado,dispatch_uid="pre_save_foto_denunciante")
def CogerFotoActual(sender, instance, **Kwargs):
	try:
		FotoDenunciado=(Foto_Denunciado.objects.get(pk=instance.pk))  #este codigo funcionara solo si ya existe una imagen asociada al agente
		Fotoactual[instance.id]=FotoDenunciado.FOTO          #de no existir quiere decir que se esta agregado un nuevo agente por lo que no existe imagen guardada aun
		
	except:
		Fotoactual.clear()
		pass										 

@receiver(post_save,sender=Foto_Denunciado,dispatch_uid="post_save_foto_denunciante")
def ComprobarFoto(sender, instance, created, **Kwargs):
	
	if created:                             #Si se esta creando u nuevo usuario seguira su camnino
		pass
	else:									#si el usuario no se esta creando quiere decir que se actualizara 
		FotoGuardada=str(instance.FOTO)
		
		FotoInicial=str(Fotoactual[instance.id])
		print 'Foto inicial %s'%FotoInicial
		print 'Foto guradada %s'%FotoGuardada
		if FotoGuardada != FotoInicial :	#para lo cual comprobaremos si se trata de una foto nueva y asi poder eliminar la foto antigua
			try:
				os.remove(os.path.join(settings.MEDIA_ROOT,FotoInicial)) #elimina la foto inicial devido a que ya a sido cambiada
				Fotoactual.clear()
			except:
				Fotoactual.clear()
				pass


@receiver(post_delete,sender=Foto_Denunciado)
def photo_delete(sender,instance,**kwargs):
	instance.FOTO.delete(False)
