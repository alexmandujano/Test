from django.db import models
from django.contrib.auth.models import User

class Denunciante(models.Model):
	COD_DENUNCIANTE=models.CharField(max_length=10)
	NOM_DENUNCIANTE=models.CharField(max_length=40)
	APELLIDO_P=models.CharField(max_length=20)
	APELLIDO_M=models.CharField(max_length=20)
	EDAD=models.IntegerField()
	DNI=models.CharField(max_length=8)
	SEXO=models.CharField(max_length=1)
	ESTADO_CIV=models.CharField(max_length=1)
	LUG_NAC=models.CharField(max_length=50, null=True, blank=True)
	OCUPACION=models.CharField(max_length=50, null=True, blank=True)
	DIRECCION=models.CharField(max_length=50, null=True, blank=True)
	USUARIO=models.OneToOneField(User,null=True)
	CONFORME=models.BooleanField(default=False,editable=True)

	def __unicode__(self):

		return self.NOM_DENUNCIANTE+' '+self.APELLIDO_P+' '+self.APELLIDO_M
  