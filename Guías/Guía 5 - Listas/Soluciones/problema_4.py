# Determina si todos los elementos de una lista son distintos

# DATOS DE ENTRADA
# Captura numeros por teclado
numeros = input("Ingrese numeros enteros separados por coma (,): ")

# PROCESAMIENTO
# Transforma la entrada de string a list
lista_numeros = numeros.split(",")
# Cada numero pasa de string a int.
for posicion in range(0,len(lista_numeros)):
    lista_numeros[posicion] = int(lista_numeros[posicion])
todos_diferentes = True
largo_lista = len(lista_numeros)
i = 0
while i < (largo_lista - 1):
    j = i + 1
    while j < largo_lista:
        if lista_numeros[i] == lista_numeros[j]:
            todos_diferentes = False
        j = j + 1
    i = i + 1

# SALIDA
if todos_diferentes:
    print("Todos los numeros de la lista son diferentes")
else:
    print("Se repite al menos un numero en la lista")
    
