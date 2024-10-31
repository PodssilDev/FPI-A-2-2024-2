# ENTRADA
numeros = input("Ingrese numeros separados por coma (,): ")

# PROCESAMIENTO
# Se transforma la entrada a lista y se transforman los numeros
# de string a int
lista_numeros = numeros.split(",")
largo_lista = len(lista_numeros)
for posicion in range(0, largo_lista):
    lista_numeros[posicion] = int(lista_numeros[posicion])

i = 0
repeticiones_numeros = []
# Se calcula cuantas veces se repite cada numero en la lista
while i < largo_lista:
    numero_actual = lista_numeros[i]
    se_repite = 0
    j = 0
    while j < largo_lista:
        numero_siguiente = lista_numeros[j]
        if numero_actual == numero_siguiente:
            se_repite += 1
        j += 1
    repeticiones_numeros.append(se_repite)
    i += 1

# Se obtiene el mayor numero de repeticiones
max_repeticiones = max(repeticiones_numeros)
k = 0
mayor_repetidos = []
# Se busca el o los numero(s) que tenga(n) el mayor numero de repeticiones
while k < largo_lista:
    if max_repeticiones == repeticiones_numeros[k]:
        # Si no se ha agregado ese numero a la lista final, se agrega
        # Si no, se salta, ya que se repite la misma informacion 
        if lista_numeros[k] not in mayor_repetidos:
            mayor_repetidos.append(lista_numeros[k])
    k += 1

# SALIDA
if len(mayor_repetidos) == 1:
    print("El numero que mas se repite es:", mayor_repetidos[0])
elif len(mayor_repetidos)> 1:
    print("La lista de numeros que mas se repiten es:", mayor_repetidos)
    
    
