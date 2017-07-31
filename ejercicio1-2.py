# coding=utf-8
'''
Ejercicio 1.2. Implementar algoritmos que permitan:
a) Calcular el perímetro y área de un rectángulo dada su base y su altura.
b) Calcular el perímetro y área de un círculo dado su radio.
c) Calcular el volumen de una esfera dado su radio.
d) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
e) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''


def calcularPerimetroRectangulo(base, altura):
    return base * 2 + altura * 2


def calcularAreaRectangulo(base, altura):
    return base * altura


def calcularAreaYPerimetro(base, altura):
    area = calcularAreaRectangulo(base, altura)
    perimetro = calcularPerimetroRectangulo(base, altura)
    print "El area es de " + str(area) + " y el perimetro es " + str(perimetro)


calcularAreaYPerimetro(3, 5)
