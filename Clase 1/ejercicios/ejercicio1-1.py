# coding=utf-8
'''
Ejercicio 1.1. Escribir un programa que pregunte al usuario:
a) su nombre, y luego lo salude.
b) dos números y luego muestre el producto.
'''


def preguntarNombre():
    nombre = raw_input("Por favor, ingrese su nombre: ")
    return nombre


def saludar(nombre):
    print "Hola " + nombre


def saludarAlUsuario():
    nombre = preguntarNombre()
    saludar(nombre)


def pedirValor():
    return raw_input("Ingrese un numero por favor: ")


def preguntarNumero():
    value = pedirValor()
    if (not value.isdigit()):
        preguntarNumero()
    else:
        return int(value)


def calcularProducto(factor1, factor2):
    return factor1 * factor2


def calcularProductoParaUsuario():
    factor1 = preguntarNumero()
    factor2 = preguntarNumero()
    print "El producto es " + str(calcularProducto(factor1, factor2))

saludarAlUsuario()
calcularProductoParaUsuario()
