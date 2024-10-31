# ENTRADAS
a = int(input("Ingrese el primero numero: "))
b = int(input("Ingrese el segundo numero: "))

# PROCESAMIENTO
resultado = 0
# Se suma a b veces
for num in range(b):
    resultado = resultado + a

# SALIDA
print(a, "*", b, "=", resultado)
