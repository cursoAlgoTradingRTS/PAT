'''
Ejercicio 1.4. Implementar un algoritmo que, dado un numero entero n, permita calcular su
factorial.
'''

def calcularFactorial(numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return numero * (calcularFactorial(numero - 1 ))


print calcularFactorial(1)
print calcularFactorial(3)
print calcularFactorial(5)
print calcularFactorial(8)
print calcularFactorial(9)
print calcularFactorial(12)
print calcularFactorial(15)
print calcularFactorial(100)