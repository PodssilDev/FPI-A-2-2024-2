# Calcula el m.c.d. entre dos numeros con euclides
# ENTRADA
dividendo = int(input("Ingrese el mayor numero: "))
divisor = int(input("Ingrese otro numero: "))

# PROCESAMIENTO
while (dividendo % divisor) != 0:
    # Guarda el divisor
    auxiliar = divisor
    # Asigna el resto al divisor
    divisor = dividendo % divisor
    # Asigna el divisor al dividendo
    dividendo = auxiliar

# SALIDA
print("El M.C.D. es: ",divisor)
