var checkboxActivado=false;
document.getElementById("seguirConectado").onclick=function()
{
	if(checkboxActivado==true)
	{
		document.getElementById("labelSeguirConectado").style.color="rgb(155, 152, 152)";
		checkboxActivado=false;
	}
	else
	{
		document.getElementById("labelSeguirConectado").style.color="black";
		checkboxActivado=true;
	}
}