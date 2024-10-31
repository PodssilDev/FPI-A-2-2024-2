# Determina si un numero es primo o compuesto
# ENTRADA
numero = int(input("Ingrese un numero mayor o igual que 2: "))

# PROCESAMIENTO
primo = True
i = 2
while i < numero:
    # Determina si el numero es divisible por i
    if numero % i == 0:
        # Cambia el valor de la bandera
        primo = False
    i = i + 1

# SALIDA
if primo:
    print("El numero", numero, "es primo")
else:
    print("El numero", numero, "es compuesto")
