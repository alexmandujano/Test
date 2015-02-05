from django.contrib import admin
from.models import Agente

class AdminAgente(admin.ModelAdmin):
	list_display=('COD_POLICIA','NOM_POLICIA','APELLIDO_P','APELLIDO_M','DNI','COMISARIA','FOTO','FotoAgente','CONFORME')
	list_filter=('CONFORME','COMISARIA')
	search_fields=('COD_POLICIA','NOM_POLICIA','APELLIDO_P','APELLIDO_M','DNI')

	def FotoAgente(self,Agente):
		url=Agente.traer_url_foto()
		tag='<img src={ruta} width={ancho}/>'.format(ruta=url,ancho=200)
		return tag

	FotoAgente.allow_tags=True

admin.site.register(Agente,AdminAgente)