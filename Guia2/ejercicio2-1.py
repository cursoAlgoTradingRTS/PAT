# coding=utf-8
'''Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés
y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
Cn = C × (1 + x/100)^n
Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.'''


def pedirPesos():
    pesos = raw_input("Ingrese una cantidad de pesos: ")
    if (not pesos.isdigit()):
        pedirPesos()
    return float(pesos)


def pedirTasa():
    tasa = raw_input("Ingrese una tasa de interes: ")
    if (not tasa.isdigit()):
        pedirTasa()
    return float(tasa)


def pedirAnios():
    anios = raw_input("Ingrese una cantidad de anios: ")
    if (not anios.isdigit()):
        pedirAnios()
    return float(anios)


def pedirParametrosYCalcular():
    pesos = pedirPesos()
    tasa = pedirTasa()
    anios = pedirAnios()
    capital = pesos * ((1 + float(tasa) / 100.0) ** anios)
    print "El capital final es de " + str(capital)


pedirParametrosYCalcular()
