"""
Django settings for Sisdepo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#Permite regresar ala ruta pricipal del proyecto
from unipath import Path
RUTA_PROYECTO=Path(__file__).ancestor(2)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-m%x8gn)su6k1qt@vn^8s@7uu4e6zkp9u(@1d%6j3uq2y6$$m5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    RUTA_PROYECTO.child('Templates'),



)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Inicio',
    'apps.Agentes_Pnp',
    'apps.Denunciado',
    'apps.Denunciante',
    'apps.ActaIntervencion',
    'apps.ActasIdentidad',
    'apps.Delito',
    'apps.Falta',
    'apps.Comisaria',
    'captcha',
    
)


CAPTCHA_BACKGROUND_COLOR = 'transparent'    #Color de fondo
CAPTCHA_FONT_SIZE =30                       #Tamano del captcha
CAPTCHA_LETTER_ROTATION=-35,35              #Rotacion de las letras
CAPTCHA_FOREGROUND_COLOR='red'              #Color del texto
CAPTCHA_TIMEOUT=1                           #Tiempo vida del captcha
CAPTCHA_LENGTH=4                            #Nro de caracteres
CAPTCHA_TEST_MODE=False                     #True se permite 'passed' para cualquier captcha
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #Case sensitive
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge' #Muestra palabrasa artir de un diccionario

CAPTCHA_CHALLENGE_FUNCT='apps.Inicio.views.MiCaptcha'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
     
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'Sisdepo.urls'

WSGI_APPLICATION = 'Sisdepo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST':'', #localhost',
        'NAME': 'sisdepo.db',#BaseSisdepo',
        'USER':'',#'sisdepo',
        'PASSWORD':'',#'12345',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Asignamos la carpeta donde se asignara los archivos multimedia(Fotos)
MEDIA_ROOT=RUTA_PROYECTO.child('media')
#Le asignamos la ruta del  del archivo media
MEDIA_URL='http://127.0.0.1:8000/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/' #esto escribiremos en nuestro html para llamar a los archivos estaticos

#Especificaos en que folder se encuentran nuestros archivos staticos 
STATICFILES_DIRS=(
    RUTA_PROYECTO.child('statics'), #Folder Static

)


#LOGIN

from django.core.urlresolvers import reverse_lazy
#redirecciona el url a la ruta login
LOGIN_URL=reverse_lazy('login')
#sirve para redireccionar a una ruta una ves se a accedido
LOGIN_REDIRECT_URL=reverse_lazy('inicio')
#ruta que tomara para cerrar la cesion
lOGOUT_URL=reverse_lazy('logout')

