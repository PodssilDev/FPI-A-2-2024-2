# ENTRADA
numeros = input("Ingrese numeros separados por coma (,): ")

# PROCESAMIENTO
# Se transforma la entrada a lista y se transforman los numeros
# de string a int
lista_numeros = numeros.split(",")
largo_lista = len(lista_numeros)
for posicion in range(0, largo_lista):
    lista_numeros[posicion] = int(lista_numeros[posicion])

# Si el numero no esta en la lista sin repetidos, se agrega el numero
# Si no, no se agrega
lista_sin_repetidos = []
for numero in lista_numeros:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

# SALIDA
print(lista_sin_repetidos)
