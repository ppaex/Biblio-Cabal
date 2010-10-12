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

Plantillas
==========

El sistema de plantillas se aproxima a ellas desde el punto de vista del diseñador. La plantilla muestra código expecífico al lenguaje para el que será destinada. BiblioCabal requiere, solamente, unos marcadores; los cuales se definen de manera compatible al lenguaje nativo a la plantilla. De esta manera, el diseñador se enfoca en diseñar la plantilla en su propio lenguaje; sin alienarse a otro.

Uso
===

 python3 biblio.py

Este programa generará varios archivos:

===========   ============        ======================
Archivo       ordenado por        plantilla
===========   ============        ======================
autor.html    autor               tabla-xhtml 
autor.xml     autor               archivo-xml
tabla.html    titulo              tabla-unica-xhtml
tabla2.html   autor               tabla-unica-tres-xhtml
tabla.tex     autor               archivo-tex
tablas.tex    autor               archivo-tablas-tex
===========   ============        ======================

Para la pagina de la biblioteca de LinuxCabal A.C. utilizamos el tercer archivo tabla.html, ordenado por titulo. Este archivo contiene solamente un elemento tabla en XHTML1 Strict, el contenido es aplicado a una `plantilla estándar`__ PHP, a la cual se le agrega el siguiente renglón: 

 include ("./tabla.html" );

El documento PHP se llama biblio.php y junto con tabla.html son copiados al servidor de linuxcabal, para estar disponibles en la dirección 
http://linuxcabal.org/PythonCabal/biblio.php

__ http://linuxcabal.org/Template.phps
