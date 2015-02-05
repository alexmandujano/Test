from django.conf.urls import patterns, include, url
from .views import BuscarDenunciado,Consulta 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sisdepo.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^buscar/', BuscarDenunciado.as_view(),name='BuscarDenunciado'),
	url(r'^consulta/(\d+)$',Consulta,name='consulta'),
	

)

