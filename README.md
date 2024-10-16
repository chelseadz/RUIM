# RUIM2022ELIXIR

Proyecto en cumplimiento de la materia Ingeniería de Software 2 en la Universidad de Sonora.
El proyecto consiste en una aplicacion web con la capacidad de ser actualizable año con año para el congreso creado por la Reunión Universitaria de Investigación en Materiales.

### Características principales de la aplicación.
* El administrador puede renovar los detalles de la conferencia año con año a traves de una interfaz.
* Los participantes de la conferencia pueden registrarse y reciben su certificado por e-mail al finalizar la conferencia, una vez que el administrador los envía.
* Las constancias de participación son generadas automaticamente desde el panel de administrador.


Pasos para instalación en servidor local.
1. Activar conda environment.yml
2. Desde la terminal con el environment activo y dento de la carpeta del proyecto ejecutar:


  py manage.py makemigrations
  
  py manage.py migrate
  
  py manage.py runserver
  
