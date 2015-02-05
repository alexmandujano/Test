from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Denunciado,Foto_Denunciado
from apps.Falta.models import Falta
#from apps.Demm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class BuscarDenunciado(LoginRequiredMixin,ListView):
	model=Denunciado
	template_name='Denunciados/buscardenunciados.html'
	context_object_name='denunciados'

	def post(self, request, *args, **kwargs):
		ParametroBusqueda=request.POST['txtbuscar']
		ListaDenunciados=Denunciado.objects.filter(Q(COD_DENUNCIADO__contains=ParametroBusqueda)|Q(DNI__contains=ParametroBusqueda)|
												   Q(NOM_DENUNCIADO__contains=ParametroBusqueda)|Q(APELLIDO_P__contains=ParametroBusqueda))
		return render(request,'Denunciados/buscardenunciados.html',
			{'denunciados':ListaDenunciados})	
		
@login_required
def Consulta(request,id_denunciado):
	denunciado=Denunciado.objects.get(pk=id_denunciado)
	fotos=Foto_Denunciado.objects.filter(DENUNCIADO=id_denunciado)
	faltas=denunciado.falta_set.all()
	delitos=denunciado.delito_set.all()
	actasidentidad=denunciado.acta_identidad_set.all()
	actasintervencion=denunciado.acta_intervencion_set.all()

	return render(request,'Denunciados/detalledenunciado.html',
			{'denunciado':denunciado,'fotos':fotos,'faltas':faltas,
			 'delitos':delitos,'actasidentidad':actasidentidad,
			 'actasintervencion':actasintervencion})
	

 

	
