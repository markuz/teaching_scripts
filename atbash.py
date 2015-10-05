#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# Hay que poner la linea shebang https://en.wikipedia.org/wiki/Shebang_(Unix)
# Coding y encoding son Necesarios para poder hacer uso de hacentos y otros 
#  caracteres no ascii.

#Escrito originalmente por Pedro Jesús González Vargas 
def contar(cad):
    # Esto lo podemos sustituir por string.letters
    #  import string
    #  string.letters
    # Debemos respetar el PEP-8 y no escribir mas de 80 caracteres
    #  https://www.python.org/dev/peps/pep-0008/
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
            "R","S","T","U","V","W","X","Y","Z"]
    # abc lo pudimios inicializar como una lista en lugar de una tupla.
    o=list(abc)
    o.reverse()
    b={}
    for i in range(len(abc)):
        b[str(abc[i])]=i
    result = ""
    for i in cad:
        result += o[int(b[i])]
    print result
contar("KVWIL")
    
    
 

