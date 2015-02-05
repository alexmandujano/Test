$(function()
{
	//Script de las imagenes que cambian
	$("#contenedor_imagen_pequeno img").click(function()
	{
		$("#contenedor_imagen_pequeno img").css("opacity","0.5");
		$(this).css("opacity","1");
		$url_imagen_seleccionada=$(this).attr("src");
		$("#imagen_principal").attr("src",$url_imagen_seleccionada);

	});

	//Script para que salga en detalle los antecedentes
	$("table .tabla_antecedentes_datos td").click(function()
	{
		$varlorDisplay=$($(this).parent()).next().css("display");
		if($varlorDisplay=="table-row")
		{
			//ocultar
			$($(this).parent()).next().css("display","none");
		}
		else
		{
			//mostrar
			$($(this).parent()).next().css("display","table-row");
		}
	});
});