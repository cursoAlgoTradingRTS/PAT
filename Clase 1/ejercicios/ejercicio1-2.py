# coding=utf-8
'''
Ejercicio 1.2. Implementar algoritmos que permitan:
a) Calcular el perímetro y área de un rectángulo dada su base y su altura.
b) Calcular el perímetro y área de un círculo dado su radio.
c) Calcular el volumen de una esfera dado su radio.
d) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
e) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''

#Debo importar la libreria Math que provee de funciones matematicas adicionales
import math
#Tomo pi de la libreria
PI = math.pi

def calcularPerimetroRectangulo(base, altura):
    return base * 2 + altura * 2


def calcularAreaRectangulo(base, altura):
    return base * altura


def calcularAreaYPerimetroRectangulo(base, altura):
    area = calcularAreaRectangulo(base, altura)
    perimetro = calcularPerimetroRectangulo(base, altura)
    print "El area es de " + str(area) + " y el perimetro es " + str(perimetro)


calcularAreaYPerimetroRectangulo(3, 5)


def calcularPerimetroCirculo(radio):
    return radio*2.0*PI

def calcularAreaCirculo(radio):
    return PI*(radio**2)

def calcularAreaYPerimetroCirculo(radio):
    area = calcularAreaCirculo(radio)
    perimetro = calcularPerimetroCirculo(radio)
    print "El area es de " + str(area) + " y el perimetro es " + str(perimetro)

calcularAreaYPerimetroCirculo(4)


def calcularVolumenEsfera(radio):
    volumen = (4/3)*PI*(radio**3)
    print "El volumen de la esfera de radio " + str(radio) + " es de " + str(volumen)

calcularVolumenEsfera(5)


def calcularAreaRectanguloConCoordenadas(x1, y1, x2, y2):
    lado1 = abs(x2-x1)
    lado2 = abs(y2-y1)
    area = lado1 * lado2
    print "El area es de " + str(area)
    return area

calcularAreaRectanguloConCoordenadas(1,3,2,5)

def calcularHipotenusa(cateto1, cateto2):
    sumaCatetosCuadrado = cateto1**2 + cateto2**2
    raiz = math.sqrt(sumaCatetosCuadrado)
    print "La hipotenusa es " + str(raiz)
    return  raiz

calcularHipotenusa(3,4)
