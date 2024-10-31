# ENTRADA
texto = input("Ingrese una secuencia de numeros separados por espacios: ")

# PROCESAMIENTO
lista_numeros = texto.split(" ")
i = 0
while i < len(lista_numeros):
    lista_numeros[i] = int(lista_numeros[i]) ** 2
    lista_numeros[i] = str(lista_numeros[i])
    i = i + 1

secuencia_salida = ", ".join(lista_numeros)

# SALIDA
print(secuencia_salida)
