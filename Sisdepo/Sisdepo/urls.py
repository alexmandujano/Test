from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from apps.Inicio.views import Cambiar
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sisdepo.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('apps.Inicio.urls')), 
	#url(r'^agente/', include('apps.Agentes_Pnp.urls'),name='agente')
	#esto nos permitira acceder por medio de urls a las imagenes que tenemos en nuestro archivo media
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
    	{'document_root' : settings.MEDIA_ROOT, } ),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^denunciado/',include('apps.Denunciado.urls')),
)
