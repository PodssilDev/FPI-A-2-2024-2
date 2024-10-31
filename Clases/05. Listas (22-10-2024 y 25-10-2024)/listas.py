lista_numeros = [3,4,1,6,3,2,6,7,2,1,8,2,8]
lista_unicos = []
i = 0
while i < len(lista_numeros):
    numero_actual = lista_numeros[i]
    if numero_actual not in lista_unicos:
        lista_unicos.append(numero_actual)
    i += 1

minimo = lista_unicos[0]
i = 0
lista_ordenados = []
while i < len(lista_unicos):
    numero_actual = lista_unicos[i]
    if numero_actual < minimo:
        minimo = numero_actual
    i += 1


