# coding=utf-8
'''
Ejercicio 2.3. Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde
0◦F hasta 120 ◦F, de 10 en 10.
'''


def convertCelsiusToFarenheit(celsius):
    value = (9 / 5) * celsius + 32
    return value


def tablaConversion():
    for x in range(0, 100, 10):
        value = convertCelsiusToFarenheit(x)
        print x, value


tablaConversion()
