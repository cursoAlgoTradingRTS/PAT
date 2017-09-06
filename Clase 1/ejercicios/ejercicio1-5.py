# coding=utf-8
'''Ejercicio 1.5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es: F = (9/5)C + 32'''


def convertCelsiusToFarenheit(celsius):
    value = (9 / 5) * celsius + 32
    return value


print "0 celsius son " + str(convertCelsiusToFarenheit(0)) + " Farenheit"
print "10 celsius son " + str(convertCelsiusToFarenheit(10)) + " Farenheit"
print "25 celsius son " + str(convertCelsiusToFarenheit(25)) + " Farenheit"
print "100 celsius son " + str(convertCelsiusToFarenheit(100)) + " Farenheit"
