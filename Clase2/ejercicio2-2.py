# coding=utf-8
'''
 Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces,
con espacios intermedios.
'''


def pedirPalabra():
    palabra = raw_input("Ingrese una palabra por favor: ")
    return palabra


palabra = pedirPalabra()

for i in range(1000):
    print palabra,
