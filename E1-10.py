# -*- coding: utf-8 -*-
""" E1
All natural numbers divisible by 5 or 7 less than 20 are {} The sum of these number is 51. In this exercise, we treat zero as a natural number.

Find the sum of all numbers that are divisible by 5 or 7 less than 100

Present the solution in the form of a function called calculate. In response, call calculate functional and print the result to the console
"""

"""
def calculate():
    suma=0
    for i in range(0,100):
        if i%5==0 or i%7==0:
          suma+=i
    print(suma)
    return suma

def calculate2():
    return sum([x for x in range(0,100) if x%5==0 or x%7==0])

print(calculate2())
"""


""" E2
Consider the fibonacci sequence. It is a sequence of natural numbers defined recursively as follows
1 the first element of the sequence is 0
2 the second element of the sequence is 1
3 each next element of the sequence is the sum of the previous two elemnts 

The beginning of the fibonacci sequence
0 1 ....

Find the sum of all elements of the fibonacci sequence with values less than 1 million

Present the solution in the form of a function called calculate(). In response, call calculate function and print the result to the console
"""

"""

def calculate():
    total = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

print(calculate())

"""

""" E3
En la teoría de números, la factorización de enteros es la descomposición de un número compuesto en un producto de enteros menores. Si estos factores se restringen aún más a los números primos, el proceso se denomina descomposición en factores primos.

Ejemplos de números primos: 2 3 5 7 11

Recordatorio: el número 1 no es un número primo

Un número que es mayor que 1 y no es primo se llama número compuesto.

Ejemplos de número compuesto en factores primos. Por ejemplo:
15=3*5
36=2*2*3*3
48=2*2*2*2*3

Implemente una función que tome un número natural como argumento y devuelva una lista que contenga la descomposición en factores primos de ese número. Presentar la solución en forma de una función llamada calcular()
"""

"""
def calculate(n):
    lista=[]
    i=2
    while n!=1:
        if n%i==0:
            lista.append(i)
            n/=i
            i=2
        else:
            i+=1
    return lista
    
print(calculate(48))
"""


""" E4
En teoría de números, la factorización de números enteros es la descomposición de un número compuesto en un producto de números enteros más pequeños. Si estos factores son números primos más restringidos, el proceso se llama descomposición en factores primos.

Ejemplos de números primos: 2 3 5 7 11
Recordatorio: el número 1 no es un número primo

Un número que es mayor que 1 y no es primo se llama número compuesto

Ejemplos de números compuestos: 4 6 8 9 10

Podemos descomponer un número de composición en factores primos. Por ejemplo:
15=3*5
36=2*2*3*3

El factor primo más grande para 15 es 5, y para 36 es 3

Usando el ejercicio anterior, implemente una función que tome un número natural como argumento y devuelva el mayor factor primo de ese número. Presente la solución en forma de una función llamada calcular ()

Solo necesitas implementar la función. Las pruebas ejecutan varios casos de prueba para validar la solución.
"""

"""
def calculate(n):
    lista=[]
    i=2
    while n!=1:
        if n%i==0:
            lista.append(i)
            n/=i
            i=2
        else:
            i+=1
    return max(lista)
    
print(calculate(13195))
"""


""" E5
Considere los números palindrómicos. Un número palindrómico o simétrico es un número que no cambia cuando escribes sus dígitos en orden inverso.

Algunos ejemplos de números palindrómicos:
363
2882
29492

Implemente una función que devuelva el número de todos los números panlindrómicos de tres dígitos. Presente la solución en forma de una función llamada calcular(). En respuesta, llame a la función de cálculo () e imprima el resultado en la consola
"""

"""
def calculate():
 numbers = []
 for i in range(100, 1000):
     if str(i) == str(i)[::-1]:
         numbers.append(i)
 return len(numbers)
 
 
print(calculate())
"""



""" E6
Considere los números palindrómicos. Un número palindrómico o simétrico es un número que no cambia cuando escribes sus dígitos en orden inverso.
Algunos ejemplos de números palindrómicos:
363
2882
29492
Implementa una función que devuelva el mayor número palindrómico resultante del producto de números de dos dígitos.
Presente la solución en forma de una función llamada calcular(). En respuesta, llame a la función de cálculo e imprima el resultado en la consola
"""

"""
def calculate():
    mayor=0
    for i in range(10,100):
        for j in range(10,100):
            if str(i*j)==str(i*j)[::-1]:
                mayor=i*j
    return mayor

print(calculate())



def calculate2():
    result = max([i * j
                  for i in range(10, 100)
                  for j in range(10, 100)
                  if str(i * j) == str(i * j)[::-1]])
    return result
 
 
print(calculate2())
"""


""" E7
Máximo común divisor MCD de dos enteros: este es el mayor número natural que divide a ambos números sin dejar resto
Por ejemplo, de los números 32 y 48, el máximo común divisor es 16, que podemos escribir MCD(32,48)=16
Implemente una función llamada great_common_divisor() que determine el máximo común divisor de dos números
MCD(32,48)
dieciséis

Solo necesitas implementar la función. La prueba de varios casos de prueba para validar la solución.
https://stackoverflow.com/questions/14994266/cant-understand-codes-for-def-gcd
"""

"""
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
        
print(greatest_common_divisor(-8,-16))
"""


""" E8
Un número primo es un número natural mayor que 1 que no es producto de dos números naturales menores.
Ejemplo de números primos: 2 3 5 7 11 13 17 19
Implemente una función llamada is_prime() que tome un número natural como argumento y verifique si es un número primo. En el caso de un número primo, el caso de un número primo, la función devuelve Verdadero, de lo contrario Falso
Ejemplo
es_principal(11)
Verdadero

Solo necesitas implementar la función. la prueba ejecuta varios casos de prueba para validar la solución
"""

"""
def is_prime(n1):
    if n1%2==0:
        return False
    for i in range (3,n1,2):
        if n1%i==0:
            return False
    return True
print(is_prime(79))

def is_prime2(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print(is_prime2(79))
"""


""" E9
Un número primo es un número natural mayor que 1 que no es producto de dos números naturales menores.
Ejemplos de números primos 2 3 5 7 11 13
El número primo en la posición uno es 2. El número primo en la posición dos es 3. El número primo en la posición tres es 5. Implemente una función que devuelva un número primo en la posición 100
En la solución, usa la función is_prime() del ejercicio anterior:

Presente la solución en forma de una función llamada función de cálculo () e imprima el resultado en la consola
541
"""

"""
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def calculate():
    cont=0
    i=2
    while cont<100:
        if is_prime(i):
            cont+=1
        i=i+1
    return i
        
print(calculate())
"""


""" E10
Condifer los números palindrómicos. Un número palindrómico o simétrico es un número que no cambia cuando escribes sus dígitos en orden inverso

Algunos ejemplos de número palindrómico:
363
Implemente una función llamada is_palindrome() que verifique si el número pasado es palindrómico decimal y binario

Por ejemplo, el número 99 es un número palindrómico y su notación binaria 1100011 también es palíndromo. Cuando se cumplen estas condiciones, la función devuelve True, de lo contrario False
"""

"""
def is_palindrome(n):
    if str(n)==str(n)[::-1] and str(format(n,"b"))== str(format(n,"b"))[::-1]:
        return True
    
print(is_palindrome(99))
"""










