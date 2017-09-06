# coding=utf-8
'''
Ejercicio 2.1. Implementar algoritmos que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número entero n, imprimir su tabla de multiplicar.
c)Implementar un algoritmo que, dado un numero entero n, permita calcular su
factorial.
'''


def sumaDosNumeros(num1, num2):
    return num1 + num2

def restaDosNumeros(num1, num2):
    return num1 - num2

#Ojo que esta division devuelve el valor entero de la misma, si se quiere obtener el valor con decimales hay que convertir los numeros a punto flotante
def dividir(dividendo, divisor):
    return dividendo/divisor

def multiplicar(num1, num2):
    return num2*num1


def imprimirOperacionesMatematicas(num1, num2):
    print "Suma " + str(sumaDosNumeros(num1, num2))
    print "Resta " + str(restaDosNumeros(num1, num2))
    print "Division " + str(dividir(num1, num2))
    print "Multiplicacion " + str(multiplicar(num1, num2))

imprimirOperacionesMatematicas(25,4)


def tablaMultiplicar(numero):
    for x in range(10):
        multiplo = x+1
        print str(multiplo) + " x " + str(numero) + " = " + str(multiplo*numero)

tablaMultiplicar(8)


# resolucion en forma iterativa
def factorialIterativo(numero):
    factorial = 1
    for i in range(1, numero + 1, 1):
        factorial = factorial * i
    return factorial


# resolucion en forma recursiva
def calcularFactorial(numero):
    if (numero == 0 or numero == 1):
        return numero
    else:
        return numero * (calcularFactorial(numero - 1))


print calcularFactorial(1)
print calcularFactorial(3)
print calcularFactorial(5)
print calcularFactorial(8)
print calcularFactorial(9)
print calcularFactorial(12)
print calcularFactorial(15)
print calcularFactorial(100)

print factorialIterativo(1)
print factorialIterativo(3)
print factorialIterativo(5)
print factorialIterativo(8)
print factorialIterativo(9)
print factorialIterativo(12)
print factorialIterativo(15)
print factorialIterativo(100)
