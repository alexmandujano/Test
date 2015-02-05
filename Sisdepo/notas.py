Instalar PostgrestSql con Django en Ubuntu:

1.- instalar PostgrestSql
Terminal: 
sudo apt-get install postgresql
2.- Instalar depedencias del conector psycopg2
Terminal:
sudo apt-get build-dep python-psycopg2
3.- Instalar el psycopg2
Terminal :
pip install psycopg2
o
sudo apt-get install psycopg2

Configurando PostgrestSql

Terminal:

velocidad@mi-equipo:~$ sudo su - postgres
postgres@mi-equipo:~$ createuser -s -r velocidad
postgres@mi-equipo:~$ psql
postgres=# ALTER USER velocidad WITH ENCRYPTED PASSWORD 'password';
posrgres=# \q 
postgres@mi-equipo:~$ exit
velocidad@mi-equipo:~$ createdb mibasededatos

Settings de Django.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mibasededatos',
        'USER': 'velocidad',
        'PASSWORD': 'password',
        'HOST': 'localhost', #esto es muy importante
        'PORT': '',
    },
}

Instalando pgadmin para manejar el postgres

sudo apt-get install postgresql pgadmin3

luego buscas pg admin 3 e inicias una nueva conexion.

name= 'conexion postgres'cualquien nombre que identifique ala conexion
hot='localhost'
Maintenance DB='mibasededatos ' nombre de la base de datos
Username='velocidad'
PASSWORD= 'password'

luego enter y listo ! =D

---ver elmodelo de tu base de datos:
python manage.py inspectdb



---Matar un puerto cuando el servidor esta ocupado


#Encontrar el proceso que esta usando el puerto que queremos utilizar:
	
$ sudo netstat -lpn | grep :8000

#Si realmente está siendo usado el puerto escrito deberemos obtener una salida similar a esta:
	
tcp  0  0  127.0.0.1:8000  0.0.0.0:*  LISTEN  19663/python 

#Ya hemos detectado que el id del proceso que está usando el puerto 8000 es el 19663.
#Matamos dicho proceso:
$ kill 19663
o
$fuser -k 8000/tcp  #8000 es el puerto que queremos cerrar