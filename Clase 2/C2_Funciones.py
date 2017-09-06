# coding=utf-8

def fib(n):    # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

a = 100

def prueba1(a):
    a = 3

    def prueba2(b):

        print a

    prueba2(a)


# Ahora llamamos a la funcion que acabamos de definir:
prueba1(3)