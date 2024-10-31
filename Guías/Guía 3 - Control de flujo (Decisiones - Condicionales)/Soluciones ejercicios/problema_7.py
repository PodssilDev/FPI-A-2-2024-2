# ENTRADAS
# Pide tres numeros y los imprime de mayor a menor
# Solicita los numero a ordenar
a = float(input("Ingrese un primer numero: "))
b = float(input("Ingrese un segundo numero: ")) 
c = float(input("Ingrese un tercer numero: "))

# PROCESAMIENTO
if a >= b and a >= c:
    if b >= c:
        # SALIDA
        print("El orden de los numeros es :",a,b,c) 
    else:
        # SALIDA
        print("El orden de los numeros es :",a,c,b)
elif b >= a and b >= c:
    if a >= c:
        # SALIDA
        print("El orden de los numeros es :",b,a,c)
    else:
        # SALIDA
        print("El orden de los numeros es :",b,c,a)
else:
    if a >= b:
        # SALIDA
        print("El orden de los numeros es :",c,a,b)
    else:
        # SALIDA
        print("El orden de los numeros es :",c,b,a)
