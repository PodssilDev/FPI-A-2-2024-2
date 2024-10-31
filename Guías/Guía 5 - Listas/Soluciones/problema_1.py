# DATOS DE ENTRADA
numero_palabras = int(input("Ingrese el numero de palabras de la lista: "))

# PROCESAMIENTO 
lista_palabras = []
i = 0
while i < numero_palabras:
    palabra_ingresada = input("Ingrese una palabra: ")
    lista_palabras.append(palabra_ingresada)
    i = i + 1

# SALIDA
i = 0
while i < numero_palabras:
    print(lista_palabras[i])
    i = i + 1

