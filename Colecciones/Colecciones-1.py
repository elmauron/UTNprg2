
# MAP
# La funcion map aploca una funcion a cada campo
# iterable de una lista y devuelve el resultado.

# map( una_funcion , una_lista )

# -----------------EJEMPLO 1-------------------------------------

names = ['Pedro', 'Juan', 'Nicolas', 'Ricardo', 'Delfina', 'Sol']
lenghts = list(map(len, names))
print(lenghts)  # Output: una lista con la cantidad de letras en cada elemento.

# -----------------EJEMPLO 2-------------------------------------


def square(x):
    return x**2


cuadrados = list(map(square, range(10)))
print(cuadrados)

# ----------------------------------------------------------------
# LAMBDA
# Una funcion en python se define con la palabra
#  reservada def. Sin embargo, una funcion anonima se define con
#  la palabra reservada lambda.

# lambda parámetros : expresión
# Son funciones que pueden definir cualquier numero de paramentros pero una unica expresion.
# Esta expresion es evaluada y devuelta.
# Se pueden usar en cualquier lugar en el que una funcion sea requerida.
# Estas funciones estan restringidas al uso de una sola expresión.
# Se suelen usar en combinacion con otras funciones, generalmente como argumentos de otra función.

# -----------------EJEMPLO 1-------------------------------------

# def cuadrado(x):
#     return x**2          <------ es lo mismo que:

print((lambda x: x**2)(5))

# -----------------EJEMPLO 2-------------------------------------

elevados = list(map(lambda x: x**2, range(20)))
print(elevados)

# -----------------EJEMPLO 3-------------------------------------

print((lambda x: x.startswith('B'))('Bob'))

# ----------------------------------------------------------------
# FILTER
# La funcion filter() filtra una lista de elementos
# para los que una funcion devuelve de una lista dada.

# filter( una_funcion , una_lista )

# sacar numeros pares

pares = list(filter(lambda x: x % 2 == 0, range(10)))
print(pares)

# sacar nombres que empiecen con una letra de una lista

print(list(filter(lambda x: x.startswith('D'), names)))
