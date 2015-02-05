from django.contrib import admin
from .models import Denunciado,Foto_Denunciado

class AdminFotoDenunciado(admin.TabularInline):
	model=Foto_Denunciado
	#readonly_fields = ('FOTO',)
	extra=1

class AdminDenunciado(admin.ModelAdmin):
	list_display=('COD_DENUNCIADO','NOM_DENUNCIADO','APELLIDO_P','APELLIDO_M','EDAD','DNI','CARACTERISTICAS','DIRECCION','Foto')
	list_filter=('ESTADO_CIV',)
	search_fields=('NOM_DENUNCIADO','APELLIDO_P','APELLIDO_M','DNI')
	#raw_id_fields=('COD_DENUNCIADO',)
	inlines=(AdminFotoDenunciado,)

	def Foto(self,Denunciado):
		url=Denunciado.traer_url_foto()
		if url=='No tiene imagen':
			tag='<img src=http://127.0.0.1:8000/media/foto_denunciado/NoDisponible.png width=%s/>'%200
		else:
			tag='<img src={ruta} width={ancho}/>'.format(ruta=url,ancho=200)
		return tag

	Foto.allow_tags=True

admin.site.register(Denunciado,AdminDenunciado)
