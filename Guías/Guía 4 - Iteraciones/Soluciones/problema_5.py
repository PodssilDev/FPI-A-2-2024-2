# ENTRADA  
numero = int(input("Ingrese un numero natural: "))

# PROCESAMIENTO
factorial = 1
while numero > 1:
    factorial = factorial * numero
    numero = numero - 1
    
# SALIDA
print("El factorial del numero ingresado es:", factorial)

