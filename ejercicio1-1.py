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


saludarAlUsuario()
