from django.db import models
from apps.Denunciante.models import Denunciante
from apps.Denunciado.models import Denunciado
from apps.Agentes_Pnp.models import Agente
from apps.Comisaria.models import Comisaria
class Acta_Identidad(models.Model):
	COMISARIA=models.ForeignKey(Comisaria)
	NOM_DENUNCIANTE=models.ManyToManyField(Denunciante, blank=True, null=True)
	NOM_DENUNCIADO=models.ManyToManyField(Denunciado, blank=True, null=True)
	NRO_ACTA=models.IntegerField(blank=True, null=True)
	FECHAINI=models.DateTimeField(blank=True, null=True)
	FECHAFIN=models.DateTimeField(blank=True, null=True)
	MOTIVO=models.CharField(max_length=12, blank=True, null=True)
	ASPECTO=models.CharField(max_length=12, blank=True, null=True)
	DILIGENCIA=models.CharField(max_length=12, blank=True, null=True)
	RESULTADOS=models.TextField(blank=True, null=True)
	NOM_POLICIA=models.ForeignKey(Agente, blank=True, null=True)

	def __unicode__(self):
		
		return 'Acta de Identidad' 