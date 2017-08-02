# coding=utf-8
'''
Ejercicio 1.5. Implementar algoritmos que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número entero n, imprimir su tabla de multiplicar.
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