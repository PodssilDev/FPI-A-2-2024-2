'''
Construya un programa en Python que solicite una
cantidad de números enteros (n) y luego pida al usuario cada número
y los agregue a una lista, para luego imprimir la lista
'''

# DATOS DE ENTRADA
numero_palabras = int(input("Ingrese el número de palabras de la lista: "))

# PROCESAMIENTO
lista_palabras = []   
i = 0
while i < numero_palabras:
    palabra_ingresada = int(input("Ingrese una palabra: "))
    lista_palabras.append(palabra_ingresada)
    i = i + 1

# SALIDA
i = 0
while i < numero_palabras:
    print(lista_palabras[i])
    i = i + 1
minimo = min(lista_palabras)
print("El numero minimo de la lista es:", minimo)
maximo = max(lista_palabras)
print("El numero maximo de la lista es:", maximo)
suma = sum(lista_palabras)
print("La suma de los elementos de la lista es:", suma)






