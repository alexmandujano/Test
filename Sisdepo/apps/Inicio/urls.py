from django.conf.urls import patterns, include, url
from .views import Conforme #,Cambiar,EditarClave
urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'Sisdepo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#forma para una vista-funcion
	#url(r'^',Inicio),
	#forma para una template
	url(r'^$','django.contrib.auth.views.login',{'template_name':'Inicio/index.html'},name='login'),
	url(r'^password_change/$','django.contrib.auth.views.password_change',{'post_change_redirect':'inicio'}, name='password_change'),
	#url(r'^cambiar/$',Cambiar),
	url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
	url(r'^inicio/',Conforme,name='inicio'),
	url(r'^cambiar/',Conforme,name='inicio'),
	#url(r'^EditarClave/',EditarClave,name='EditarClave'),
)