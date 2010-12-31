import yaml

import re

class alternate( str ):
    'Alterna por los elementos.'
    def __init__( self, cadena ):
        self.lista = cadena.split( '<!-- alternate -->' )
        self.n = 0

    def __repr__( self ):
        'Override'
        value = self.lista[self.n]
        self.n = (self.n + 1) % len(self.lista)
        return value

    def format( self, *params, **keywords ):
        'Override'
        value = self.lista[self.n]
        self.n = (self.n + 1) % len(self.lista)
        return value.format( *params, **keywords )

def carga_plantilla( template ):
    'Lee y separa el archivo plantilla, regresa tres partes'

    nombre_archivo = template
    # abrir template correspondiente
    template = open("templates/" + template + '.tpl', 'r').read()
    # separar en partes
    inicio, template, final = re.split( '<!--   -->|\n% section\n', template )
    # escapar { y } propios de .tex
    if 'tex' in nombre_archivo:
        template = template.replace( '{', '{{' )
        template = template.replace( '}', '}}' )
        template = template.replace( '((', '{' )
        template = template.replace( '))', '}' )
    # manejar valores cambiantes, si los hay
    template = alternate( template )
    return inicio, template, final

def traducir_contenido( nombre_archivo, obra ):
    ''''Regresa obra con algunos caracteres convertidos
    si hace falta según el formato.'''

    obra = obra.copy()
    # Convertir & para TeX
    if '.tex' in nombre_archivo:
        for key, item in obra.items():
          if type(item) is str:
            obra[key] = obra[key].replace( '&', 'and' )
    # Convertir & para XML
    if '.xml' in nombre_archivo:
        for key, item in obra.items():
          if type(item) is str:
            obra[key] = obra[key].replace( '&', '&amp;' )
    # Convertir & y < para [X]HTML
    if '.html' in nombre_archivo:
        for key, item in obra.items():
          if type(item) is str:
            obra[key] = obra[key].replace( '&', '&amp;' )
            obra[key] = obra[key].replace( '<', '&lt;' )
    return obra


# abrir base de datos (yaml)
f = open('biblio.yaml')

# importarla a un objeto
obras = yaml.load(f)

# generar archivos según el tipo de template
def genera(llave, nombre_archivo, template):
    
    # abrir archivo a escribir
    salida = open(nombre_archivo, 'w')

    # indicar una llave para ordenar
    obras.sort(key = lambda elemento: elemento[llave])

    # cargar plantilla
    inicio, template, final = carga_plantilla( template )

    print( inicio, file = salida)
    for obra in obras:
        obra = traducir_contenido( nombre_archivo, obra )
        print(template.format( **obra ), file = salida)
    print( final, file = salida)
    
genera('Autor', 'autor.html', 'tabla-xhtml')
genera('Autor', 'autor.xml', 'archivo-xml')
genera('Título', 'tabla.html', 'tabla-unica-xhtml')
genera('Autor', 'tabla2.html', 'tabla-unica-tres-xhtml')
genera('Autor', 'tabla.tex', 'archivo-tex')
genera('Autor', 'tablas.tex', 'archivo-tablas-tex')
