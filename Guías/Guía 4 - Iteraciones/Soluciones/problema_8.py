# ENTRADA
numero = int(input("Ingrese un numero: "))

# PROCESAMIENTO
pares = 0
impares = 0
if numero == 0:
    pares = 1

while numero > 0:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    numero = numero // 10

# SALIDA
print("El numero de digitos pares es", pares, "y de impares es", impares)
