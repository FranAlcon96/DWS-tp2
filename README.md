# Tp2--Ordenadores Alcón 
### Aplicación destinada a la gestión de una tienda de ordenadores.

# Requisitos.

* Un servidor apache en funcionamiento, con el módulo cgi activado. En el caso de que no esté activado lo puede hacer mediante la instrucción: sudo a2enmod cgi, y luego reinicie o recargue el servidor.

* El intérprete de perl. 

* La base de datos MySQL. Al principio del scritp puede encontrar una serie de parámetros que corresponden a los datos de conexión, por lo que los puede modificar según sea su necesidad. Usted puede elegir la base de datos que desee, aunque recomiendo crear una llamada tp2, para evitar confusiones. Por último debe ejecutar el script adjuntado en el proyecto, el cual proporciona la tabla ordenadores, que es con la que trabajará el script.

* El módulo perl DBI, el cual permite al script conectarse a la base de datos. Lo puede instalar mediante la instrucción
