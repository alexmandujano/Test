from django.contrib import admin
from .models import Delito,TipoDelito

class ModelDelito(admin.ModelAdmin):
	list_display=('NRO_DELITO','TIPO_DELITO','COMISARIA','DENUNCIADOS','NOM_POLICIA','FECHA')
	list_filter=('NRO_DELITO','TIPO_DELITO','FECHA')
	search_fields=('NOM_DENUNCIADO__NOM_DENUNCIADO','NOM_DENUNCIADO__DNI','NOM_DENUNCIADO__APELLIDO_P',
			       'NOM_DENUNCIANTE__NOM_DENUNCIANTE','NOM_DENUNCIANTE__DNI','NOM_DENUNCIANTE__APELLIDO_P','NRO_DELITO','NOM_POLICIA__NOM_POLICIA')
	filter_horizontal=('NOM_DENUNCIADO','NOM_DENUNCIANTE')
	raw_id_fields=('NOM_POLICIA',)
admin.site.register(Delito,ModelDelito)
admin.site.register(TipoDelito) 