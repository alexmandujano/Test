/*Validado desde javascript*/
document.getElementById("form_nueva_contrasenna").onsubmit=function()
{
	var nueva_contra=document.getElementById("nueva_contra").value;
	var repetir_nueva_contra=document.getElementById("repetir_nueva_contra").value;
	cantidad_nueva_contra=nueva_contra.length;
	cantidad_repetir_nueva_contra=repetir_nueva_contra.length;
	if(cantidad_nueva_contra<6 || cantidad_repetir_nueva_contra<6)
	{
		alert("La nueva contraseña debe tener como mínimo 6 caracteres.");
		return false;
	}

	if(nueva_contra!=repetir_nueva_contra)
	{
		alert("No coincide la nueva contraseña.");
		return false;
	}

}