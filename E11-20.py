# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:23:04 2022

@author: EROS
"""

""" E11
Considere los números palindrómicos. Números palindrómicos. Un número palindrómico o simétrico es un número que no cambia cuando escribes sus dígitos en orden inverso
Algunos ejemplos de números palindrómicos:
363
Se implementa una función llamada is_palindrome() que verifica si el número es palindrómico en notación decimal y binaria
Implemente una función llamada calculate() que devuelva todos los números palindrómicos de tres dígitos en notación decimal y binaria. En respuesta, llame a la función de cálculo () e imprima el resultado en la consola
[313,585,717]

https://www.programiz.com/python-programming/methods/built-in/filter
"""

"""
def is_palindrome(n):
    if str(n)==str(n)[::-1] and str(format(n,"b"))== str(format(n,"b"))[::-1]:
        return True

def calculate():
    return [x for x in range(100,1000) if is_palindrome(x)]

def calculate2():
    return list(filter(is_palindrome, [i for i in range(100, 1000)]))

print(type(calculate()))
"""



""" E12
Considere un algoritmo de compresión de números simple que funciona de la siguiente manera:
111155522500 -> [('1',4),('5',3),('2',2),('5',1),('0',2)]
El algoritmo va de izquierda a derecha a través de cada dígito y devuelve una lista de tuplas de dos elementos. Cada tupla consta de un dígito y el número de repeticiones de un dígito dado hasta que se encuentra el siguiente dígito diferente en el número.
implemente una función llamada compress() que comprime el número como se describe arriba.
Ejemplos
comprimir(111)
[('1',3)]
Sugerencia: Puede usar el módulo integrado de itertools y groupby en su solución.

https://www.geeksforgeeks.org/python-map-function/
https://www.geeksforgeeks.org/python-itertools/
https://www.youtube.com/watch?v=WR7mO_jYN9g
https://www.youtube.com/watch?v=p8FUoSIyIVY
https://www.youtube.com/watch?v=xzQuR8RSzwY
"""

"""
from itertools import groupby
 
    
def compress2(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    return result

def compress3(number):
    return [(key, len(list(group))) for key, group in groupby(str(number))]
      
print(compress(111155522500))
"""


""" E13
Considere un algoritmo de compresión de números simple que funciona de la siguiente manera:
111155522500 -> 14_53_22_51_02
El algoritmo va de izquierda a derecha a través del número y devuelve un objeto de tipo str. Cada dígito encontrado se almacena junto con el número de veces que ese dígito se repite hasta que se encuentra otro dígito en el número. Cada uno de estos pares está separado por el carácter '_'
implementar una función llamada compress() que comprime el número como se describe arriba
https://www.w3schools.com/python/ref_string_join.asp
"""
"""
from itertools import groupby

def compress(number):
    lista="".join([str(k)+str(len(list(g)))+"_" for k,g in groupby(str(number))])
    return lista[:-1]

print(compress(111155522500))
"""


""" E14
Considere un algoritmo de compresión de números simple que funciona de la siguiente manera:
111155522500: '1....5...2..5.0..'
El algoritmo va de izquierda a derecha a través del número y devuelve un objeto de tipo str. Cada dígito encontrado se almacena junto con la cantidad de puntos: la cantidad de veces que el dígito dado se repite hasta que encuentra el siguiente dígito diferente en el número.
Implemente una función llamada compress() que comprima el número como se describe arriba.
"""

"""
from itertools import groupby,repeat

def compress(number):
    lista="".join([str(k)+"".join([i for i in repeat('.',len(list(g)))]) for k,g in groupby(str(number))])
    return lista

print(compress(20000000))
print('2.0.......')
"""

""" E15
Considere un algoritmo de compresión de números simple que funciona de la siguiente manera:
111155522500'14_53_22_51_02'
El algoritmo va de izquierda a derecha a través del número y devuelve un objeto de tipo str. Cada dígito encontrado se almacena junto con el número de veces que ese dígito se repite hasta que se encuentra otro dígito en el número. Cada uno de estos pares está separado por el carácter '_'.
Se implementa una función llamada compress() que comprime un número como se describe arriba:
Implemente una función llamada descomprimir() que descomprime la expresión a un número
"""

"""
from itertools import groupby
 
 
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)
 
 
def decompress(compressed):
    result = [(item[0], item[1:]) for item in compressed.split('_')]
    result = [i * int(j) for i, j in result]
    return int(''.join(result))

print(decompress('14_53_22_51_02'))
"""


""" E16
Considere el problema a continuación. Tenemos una aplicación en la que en algún momento obtenemos una matriz en forma de cadena (un objeto del tipo str). Por ejemplo, la siguiente cadena:

representa una matriz de 3x3. Cada fila de la matriz se almacena en una línea separada. Cada elemento de una fila está separado de otro elemento por un espacio.

Es difícil trabajar con estas matrices y realizar algunas operaciones adicionales. Transformaremos dicha matriz en listas anidadas:
[[4,2,7],[1,5,4],[2,6,8]]


Implemente una clase llamada Matriz que tome la matriz como una cadena en el método <__init__() y establezca el valor del atributo de instancia llamado matriz como listas anidadas.
m=Matriz('3 4\n5 6')

m.matriz
[[3,4],[5,6]]
"""
"""
class Matrix:
    def __init__(self, string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in string.splitlines()
        ]

m=Matrix('3 4\n5 6')
print(m.matrix)
"""

""" E17
Considere el problema a continuación. Tenemos una aplicación en la que en algún momento obtenemos una matriz en forma de cadena (un objeto del tipo str). Por ejemplo, la siguiente cadena:

representa una matriz de 3x3. Cada fila de la matriz se almacena en una línea separada. Cada elemento de una fila está separado de otro elemento por un espacio.

Es difícil trabajar con estas matrices y realizar algunas operaciones adicionales. Transformaremos dicha matriz en listas anidadas:
[[4,2,7],[1,5,4],[2,6,8]]


Se implementa parte de una clase llamada Matrix:

Agregue una implementación del método __repr__() a la clase Matrix que es una representación formal de un objeto Matrix.

Solo necesita implementar el método __repr__(). Las pruebas ejecutan varios casos de prueba para validar la solución.
"""

"""
class Matrix:

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]
    
    def __repr__(self):
        return '\n'.join(
            [
                (' '.join([str(i) for i in row]))
                for row in self.matrix
            ]
        )


m=Matrix('3 4\n5 6')
print(m.__repr__())
"""



""" E18
Considere el problema a continuación. Tenemos una aplicación en la que en algún momento obtenemos una matriz en forma de cadena (un objeto del tipo str). Por ejemplo, la siguiente cadena:

representa una matriz de 3x3. Cada fila de la matriz se almacena en una línea separada. Cada elemento de una fila está separado de otro elemento por un espacio.

Es difícil trabajar con estas matrices y realizar algunas operaciones adicionales. Transformaremos dicha matriz en listas anidadas:
[[4,2,7],[1,5,4],[2,6,8]]


Se implementa parte de una clase llamada Matrix:

Agregue una implementación del método row() a la clase Matrix que toma el índice como argumento y devuelve el correspondiente de la matriz

Solo necesita implementar el método __repr__(). Las pruebas ejecutan varios casos de prueba para validar la solución.
"""

"""
class Matrix:
    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])
    def row(self,r):
        return self.matrix[r]
"""


""" E19
Considere el problema a continuación. Tenemos una aplicación en la que en algún momento obtenemos una matriz en forma de cadena (un objeto del tipo str). Por ejemplo, la siguiente cadena:

representa una matriz de 3x3. Cada fila de la matriz se almacena en una línea separada. Cada elemento de una fila está separado de otro elemento por un espacio.

Es difícil trabajar con estas matrices y realizar algunas operaciones adicionales. Transformaremos dicha matriz en listas anidadas:
[[4,2,7],[1,5,4],[2,6,8]]


Se implementa parte de una clase llamada Matrix:

Agregue una implementación del método column() a la clase Matrix que toma el índice como argumento y devuelve la columna correspondiente de la matriz.
"""

"""
class Matrix:

    def __init__(self, string):
        self.matrix = [[int(i) for i in row.split()] for row in string.splitlines()]

    def __repr__(self):
        return '\n'.join([(' '.join([str(i) for i in row])) for row in self.matrix])

    def row(self, index):
        return self.matrix[index]
    
    def column(self,c):
        return [x[c] for x in self.matrix]


m=Matrix('3 4\n5 6\n7 8')
print(m.column(0))
"""

""" E20
Consideremos vectores que consisten solo en unos y ceros. Supongamos también una convención adicional para representar dicho vector. Por ejemplo, un vector:

presentaremos como una secuencia:

Para los vectores así definidos, podemos determinar la distancia de Hamming. La distancia de Hamming de los vectores u y v es el número de elementos donde los vectores u y v son diferentes.

Ejemplo: La distancia de Hamming de los vectores '1100100', 1010000'es igual a 3.

Implemente una función llamada hamming_distance() que devuelva la distancia de Hamming de dos vectores. Para calcular la distancia de Hamming, los vectores deben tener la misma longitud. Si los vectores tienen diferentes longitudes, genere ValueError con el siguiente mensaje:
'Ambos vectores deben tener la misma longitud.'

https://www.geeksforgeeks.org/python-raise-keyword/#:~:text=Python%20raise%20Keyword%20is%20used,further%20up%20the%20call%20stack.
"""




def hamming_distance(v1,v2):
    if len(v1) != len(v2):
        raise ValueError('Both vectors must be the same length.')        
    hd=0
    for i in range(0,len(v1)):
        if v1[i]!=v2[i]:
            hd+=1
    return hd
    


print(hamming_distance('11000','101000'))





































