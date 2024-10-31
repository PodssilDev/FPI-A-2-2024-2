# ENTRADA 
i = 0
lista_maestra = []
while i < 2:
    numeros = input("Ingrese numeros separados por coma (,) para la sub-lista " + str(i+1) + " : ")
    lista_numeros = numeros.split(",")
    largo_lista = len(lista_numeros)
    for posicion in range(0, largo_lista):
        lista_numeros[posicion] = int(lista_numeros[posicion])
    lista_maestra.append(lista_numeros)
    i += 1

# PROCESAMIENTO
lista1 = lista_maestra[0]
lista2 = lista_maestra[1]
i = 0
numeros_comunes = []
while i < len(lista1):
    j = 0
    while j < len(lista2):
        if lista1[i] == lista2[j]:
            if lista1[i] not in numeros_comunes:
                numeros_comunes.append(lista1[i])
        j += 1
    i += 1

# SALIDA
if len(numeros_comunes) != 0:
    print("Los numeros comunes entre ambas listas son:", numeros_comunes)
else:
    print("No existen numeros comunes entre ambas listas")
