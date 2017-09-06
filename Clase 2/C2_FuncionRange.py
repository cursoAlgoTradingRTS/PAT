# coding:utf-8

# Genera una lista conteniendo progresiones aritméticas
range(10)

# Hacer que el rango empiece con otro número
range(5, 10)

# Especificar un incremento diferente
range(0, 10, 3)
# Rangos Negativos
range(-10, -100, -30)

# Combinar range() y len() para iterar sobre los índices de una secuencia
a = ['Intro', 'Programacion', 'python', 'corderito']
for i in range(len(a)):
    print i, a[i]