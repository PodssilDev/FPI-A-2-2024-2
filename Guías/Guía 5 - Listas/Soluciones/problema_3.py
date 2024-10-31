# Dada una lista de n elementos, no necesariamente ordenada, busca:
# a) El elemento menor.
# b) El elemento mayor.
# c) El promedio de los elementos en la lista.

# DATOS DE ENTRADA
# Captura una lista ingresada por teclado
numeros = input("Ingrese numeros enteros separados por coma (,): ")

# PROCESAMIENTO
# Se transforman los numeros a lista
lista_numeros = numeros.split(",")
# Cada numero es transformado a int
for posicion in range(0,len(lista_numeros)):
   lista_numeros[posicion] = int(lista_numeros[posicion])

# Asume el primer elemento de la lista como el el mayor,
# menor y suma total de la lista
mayor = lista_numeros[0]
menor = lista_numeros[0] 
suma = lista_numeros[0]
largo = len(lista_numeros)
# Inicializa la variable iterador 
i = 1
# Itera sobre la lista de numeros 
while i < largo:
   # Compara elemento actual de la lista con el valor de
   # la variable mayor 
   if lista_numeros[i] > mayor:
      mayor = lista_numeros[i]
   if lista_numeros[i] < menor:
      menor = lista_numeros[i]
   suma = suma + lista_numeros[i]    
   i = i + 1
promedio = suma / largo
# SALIDA
# Imprime las variables mayor, menor y suma 
print("El mayor numero de la lista es: ", mayor)
print("El menor numero de la lista es: ", menor)
print("El promedio de la lista de numeros es: ", promedio)

