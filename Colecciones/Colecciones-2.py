import math
from functools import reduce

notas = [1, 8, 11]

notas_sumadas = reduce(lambda a, b: a+b, notas)

print(notas_sumadas)

nums = [1, 2, 3]
letras = ['a', 'b', 'c']

print(list(zip(nums, letras)))

# ---------------------------------
# A partir de una lista X y una lista Y que son las coordenadas
# de un punto en el plano calcular el punto más cercano al origen
# ------------------------------------

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [7, 1, 3, 0, 4, 5, 20, 7, 8, 9]

puntos = list(zip(x, y))
print(puntos)

origen = reduce(lambda a, b: min(a, b), puntos)
print(origen)


# TIP: la distancia entre 2 puntos es la raiz cuadrada del primero al cuadrado + el segundo al cuadrado,
# raiz cuadrada se puede hacer con la función sqrt de la librería math de python
