Introducción
============
 
Esta es el primer proyecto de la comunidad de PythonCabal publicado en GitHub. El objetivo de este proyecto es introducirnos en la programación del lenguaje Python con la realización de este guión relativamente sencillo.

La idea es que en base a un archivo formateado en YAML que contendrá los libros de los que disponemos en LinuxCabal, se auto generen porciones de código HTML para ser insertadas dentro de otras paginas. Este código estará compuesto principalmente por tablas que estarán ordenadas, en base a una característica como año, autor, editorial o alguna otra.

Esperamos tus aportaciones y sugerencias!!!

http://www.linuxcabal.org/PythonCabal.php
http://www.python.org/
http://www.yaml.org/
http://pydev.cabal.mx/

Arquitectura
============

Se utiliza Python 3.

Para almacenar la lista de libros, se utilizó un formato YAML 1.1; se usa una secuencia de mapeos, los cuales resultan en un lista de diccionarios en Python 3.

Se implementó un sistema de plantillas con la intención de generar diferentes archivos de salida, el esquema separa el código de l vista. Las plantillas son válidas en sus lenguajes respectivos, no tiene ningún código que las invalide. Actualmente se puede producir XHTML, XML y TeX.

Se utiliza el parámetro key del método sort de las listas para escoger el campo a ordenar. Usamos una variante de cadenas que regresa diferente valor cada vez que se lee. Las platillas utiliza comentarios en sus respectivos lenguajes para separar en 3 partes: Cabeza, cuerpo y pié. Cuerpo es la parte que tiene componentes que se repiten, como el renglón de una tabla y puede tener partes alternantes, que también se indican por medio de comentarios. Los valores reemplazables se definen de acuerdo al lenguaje de salida para evitar invalidar el documento. Los datos de entrada a la plantilla se traducen de acuerdo estrictamente al estándar utilizado.
