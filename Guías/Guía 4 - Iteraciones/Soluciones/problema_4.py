# ENTRADA    
numero_menor = int(input("Ingrese un numero entero: "))
numero_mayor = int(input("Ingrese otro numero entero: "))

# PROCESAMIENTO
if numero_menor > numero_mayor:
    auxiliar = numero_menor
    numero_menor = numero_mayor
    numero_mayor = auxiliar

while numero_menor <= numero_mayor:
    if (numero_menor % 3 == 0) and (numero_menor % 5 == 0):
        # SALIDA
        print("TresCinco")
    elif numero_menor % 3 == 0:
        # SALIDA
        print("Tres")
    elif numero_menor % 5 == 0:
        # SALIDA
        print("Cinco")
    else:
        # SALIDA
        print(numero_menor)
    numero_menor = numero_menor + 1
