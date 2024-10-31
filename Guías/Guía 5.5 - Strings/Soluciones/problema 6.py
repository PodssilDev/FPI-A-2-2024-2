# Cuenta el numero total de vocales en un texto

# ENTRADA
secuencia = input("Ingrese una secuencia de palabras separadas por comas: ")

# PROCESAMIENTO
lista_palabras = secuencia.split(",")
palabras_sin_repetir = []
i = 0
while i < len(lista_palabras):
    if lista_palabras[i] not in palabras_sin_repetir:
        palabras_sin_repetir.append(lista_palabras[i])
    i = i + 1
palabras_sin_repetir.sort()
secuencia_salida = ", ".join(palabras_sin_repetir)

# SALIDA
print(secuencia_salida)
