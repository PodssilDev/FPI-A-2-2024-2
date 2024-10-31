# DATOS ENTRADA
# Solicita un número
numero = int(input("Ingrese un número: "))

# PROCESAMIENTO
# Determina si el número ingresado es par  
if (numero % 2) == 0:
    # Salida informa que el número es par
    print("El número", numero, "es par")
# Caso para el número impar  
else:
    # Salida informa que el número es impar
    print("El número", numero, "es impar")
