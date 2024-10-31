# Determina si se encuentran todos los numeros desde el numero uno
# hasta el numero n

# DATOS DE ENTRADA
# Captura numeros para formar una lista
numeros = input("Ingrese numeros separados por coma (,): "))

# PROCESAMIENTO
# Se crea a lista y se transforman los numeros de string a int
lista_numeros = numeros.split(",")
largo_lista = len(lista_numeros)
for posicion in range(0, largo_lista):
    lista_numeros[posicion] = int(lista_numeros[posicion])

todos_numeros = True
i = 1
# Itera desde 1 hasta el largo de la lista
while i <= largo_lista:
    numero_i = False
    j = 0
    # Busca en numero i en la lista
    while j < largo_lista:
        if i == lista_numeros[j]:
            numero_i = True
        j = j + 1
    # Si no encuentra el numero i en la lista modifica la bandera
    if not numero_i:
        todos_numeros = False
    i = i + 1

# SALIDA
if todos_numeros:
    print("Se encuentran todos los numeros desde 1 hasta ", largo_lista)
else:
    print("No se encuentran todos los numeros")

