# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy
from django.contrib.auth.forms import SetPasswordForm

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('username','password')

#class ChangePass(forms.Form):
#	NuevaPassword=forms.sCharField(forms.CharField(label=_("New password"),widget=forms.PasswordInput))
#	RepetirNuevaPassword=forms.CharField(label=ugettext_lazy('Repetir Nueva Contraseña') ,widget=forms.PasswordInput)
#	captcha = CaptchaField()


class ChangePass(SetPasswordForm):
	captcha = CaptchaField()




