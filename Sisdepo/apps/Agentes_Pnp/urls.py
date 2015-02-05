from django.conf.urls import patterns, include, url
from .views import Agente
urlpatterns = patterns('',
	url(r'^$', 'apps.Agentes_Pnp.views.Agente'), 
)
