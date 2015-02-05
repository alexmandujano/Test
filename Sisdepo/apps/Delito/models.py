from django.db import models
from apps.Denunciante.models import Denunciante
from apps.Denunciado.models import Denunciado
from apps.Agentes_Pnp.models import Agente
from apps.Comisaria.models import Comisaria

class TipoDelito(models.Model):
	NOMBRE=models.CharField(max_length=50)

	def __unicode__(self):
		return self.NOMBRE


class Delito (models.Model):
	COMISARIA=models.ForeignKey(Comisaria)
	NOM_DENUNCIANTE=models.ManyToManyField(Denunciante)
	NOM_DENUNCIADO=models.ManyToManyField(Denunciado, blank=True, null=True)
	NOM_POLICIA=models.ForeignKey(Agente)
	NRO_DELITO=models.IntegerField()
	FECHA=models.DateTimeField()
	CONTENIDO=models.TextField()
	RESOLUCION=models.TextField()
	TIPO_DELITO=models.ForeignKey(TipoDelito)

	def __unicode__(self):
		return str(self.TIPO_DELITO)
	
	def DENUNCIADOS(self):
		denunciados=self.NOM_DENUNCIADO.all()
		lista=" "
		for denunciado in denunciados:
			lista+= denunciado.NOM_DENUNCIADO+" "+denunciado.APELLIDO_P+ " "+denunciado.APELLIDO_M+" * "
		return lista
  