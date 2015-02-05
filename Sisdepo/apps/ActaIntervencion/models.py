from django.db import models
from apps.Denunciante.models import Denunciante
from apps.Denunciado.models import Denunciado
from apps.Agentes_Pnp.models import Agente
from apps.Comisaria.models import Comisaria

class Acta_Intervencion(models.Model):
	COMISARIA=models.ForeignKey(Comisaria)
	NOM_DENUNCIANTE=models.ManyToManyField(Denunciante, blank=True, null=True)
	NOM_DENUNCIADO=models.ManyToManyField(Denunciado, blank=True, null=True)
	NOM_POLICIA=models.ForeignKey(Agente)
	NRO_DELITO=models.IntegerField()
	FECHA=models.DateTimeField()
	CONTENIDO=models.TextField()
	RESOLUCION=models.TextField()

	def __unicode__(self):
		return 'Acta de Intervencion' 