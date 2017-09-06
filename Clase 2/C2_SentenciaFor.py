# Midiendo cadenas de texto
a = ['Algo', 'Trading', 'Python']

for x in a:
    print x, len(x)

# hacer una copia por rebanada de toda la lista
for x in a[:]:
    if len(x) > 6: a.insert(0, x)