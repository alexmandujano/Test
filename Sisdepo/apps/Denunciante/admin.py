from django.contrib import admin

from .models import Denunciante

class AdminDenunciante(admin.ModelAdmin):
	list_display=('COD_DENUNCIANTE','NOM_DENUNCIANTE','APELLIDO_P','APELLIDO_M','DNI','ESTADO_CIV','DIRECCION','CONFORME')
	list_filter=('CONFORME',)
	search_fields=('COD_DENUNCIANTE','NOM_DENUNCIANTE','APELLIDO_P','APELLIDO_M','DNI')




admin.site.register(Denunciante,AdminDenunciante)
