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
lista_unificada = []

# Recorremos ambas listas, verificando si el numero esta en
# lista_unificada, si no es asi, se agrega.
for numero in lista1:
    if numero not in lista_unificada:
        lista_unificada.append(numero)
for numero in lista2:
    if numero not in lista_unificada:
        lista_unificada.append(numero)
# SALIDA
print("La union de ambas listas sin repeticiones es:", lista_unificada)
