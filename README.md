# Django-Vue-CRUD

A continuación se describen los pasos necesarios para desplegar en local el proyecto una vez clonado el repositorio. Se da por hecho que Django está instalado globalmente o que está instalado en un entorno virtual que ha sido activado previamente. 

En el siguiente enlace se explica cómo crear un entorno virtual:
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/


1. Desde la ruta principal, realizar las migraciones de Django: 'py manage.py makemigrations' y 'py manage.py migrate'
2. Arrancar el servidor: 'py manage.py runserver'
3. Desde el navegador, acceder a la ruta 'http://localhost:8000/notes/'
