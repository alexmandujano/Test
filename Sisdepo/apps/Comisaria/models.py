from django.db import models
from django.utils.translation import ugettext_lazy as _

class Comisaria(models.Model):
	NOMBRE=models.CharField(_('Nombre de la Comisaria'),max_length=50)
	DIRECCION=models.CharField(_('Direccion'),max_length=50)
	REFERENCIA=models.TextField(_('Referencia'))
	TELEFONO=models.CharField(_('Telf. '),max_length=20)

	def __unicode__(self):
		return self.NOMBRE



