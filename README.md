## Hola! muchas gracias por descargar.
**Spanish:** Este es un proyecto sencillo hecho en Python para hacer un registro y login de usuarios con nombres y contraseñas y posteriormente que cada uno de esos usuarios pueda escribir y guardar unas notas.

**English:** This is a simple project made in Python to register and login users with user names and passwords and then each of those users can write and save some notes.

> **Spanish:** Para ejecutar el programa hay que tener instalado previamente [MySQL  Workbench](https://dev.mysql.com/downloads/installer/) o un servidor de aplicaciones web que incluya  MySQL como [Wamp](https://sourceforge.net/projects/wampserver/files/) o Xampp. Una vez en tu gestor de base de datos ejecuta el script basededatos.sql.
> 
> **English:** To run the program you must have previously installed MySQL Workbench or a web application server that includes MySQL such as Wamp or Xampp. Once in your Database manager execute copy and execute basededatos.sql.

Lo que sigue es/next steps are :

	git clone
	cd /Proyecto-notas-master
	source env/bin/activate
	pip install -r requirements.txt
	python main.py

**Nota: Probablemente, dependiente de la configuración de tu localhost tengas que modificar el puerto en el archivo */usuarios/conexion.py* , en la línea 9. Este por defecto se encuentra en el puerto 3306** 

**Note: Probably, depending on the configuration of your localhost, you will have to modify the port in the file */usuarios/conexion.py* , in line 9. Default is port 3306**