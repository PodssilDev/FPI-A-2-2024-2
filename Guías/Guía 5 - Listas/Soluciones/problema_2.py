# Busca un numero en una lista

# DATOS DE ENTRADA
numeros = input("Ingrese numeros enteros separados por coma (,): ")
numero_buscado = int(input("Ingrese el número a buscar en la lista: "))

# PROCESAMIENTO
lista_numeros = numeros.split(",")

numero_encontrado = False
i = 0
while i < len(lista_numeros):
    if numero_buscado == int(lista_numeros[i]):
        numero_encontrado = True
    i = i + 1

# SALIDA
if numero_encontrado:
    print("El numero",numero_buscado,"pertenece a la lista")
else:
    print("El numero",numero_buscado,"no pertenece a la lista")
    
