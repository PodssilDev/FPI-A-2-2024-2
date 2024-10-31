# ENTRADA
# Solicita un número
numero = int(input("Ingrese un número: "))  
# PROCESAMIENTO
# Determina si es el doble de un número impar
if (numero % 2 == 0) and (((numero // 2) % 2) == 1):
    # Informa que el número es el doble de un impar
    print(numero, "es el doble de un número impar")
# Caso contrario, el número no es el doble de un impar 
else:
    # Informa que el número no es el doble de un impar
    print(numero, "no es el doble de un número impar")
