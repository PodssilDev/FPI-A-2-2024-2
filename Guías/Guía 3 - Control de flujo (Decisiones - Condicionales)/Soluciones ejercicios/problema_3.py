# Determina si un numero es el doble de un numero impar.
# ENTRADAS
# Solicita un numero
numero = int(input("Ingrese un numero: "))

# PROCESAMIENTO
# Determina si es el doble de un numero impar
if (numero % 2 == 0) and (((numero // 2) % 2) == 1):
    # Informa que el numero es el doble de un par
    # SALIDA
    print(numero, "es el doble del numero impar")
# Caso contrario, el numero no es el doble de un par 
else:
    # Informa que el numero no es el doble de un par
    # SALIDA
    print(numero, "no es el doble de un numero impar")
