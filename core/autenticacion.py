import random


longitud = 6

def generar_Codigo(longitud):
    NUmeros = list(range(9))

    codigo = ""

    for o in range(longitud):

        codigo += str(random.choice(NUmeros))

    return codigo

codigo = generar_Codigo(longitud)

print(f"el codigo generado es el siguinete: {codigo}")
    