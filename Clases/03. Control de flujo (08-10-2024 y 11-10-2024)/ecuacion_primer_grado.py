# ENTRADAS
a = float(input("Ingrese el valor del coeficiente a: "))  
b = float(input("Ingrese el valor del coeficiente b: "))  
# PROCESAMIENTO
# Determina si coeficiente a es distinto a cero  
if a != 0:
    solucion = -b / a
    # Salida
    print("La solución de la ecuación es: ", solucion)
# Determina si coeficiente b es igual a cero 
elif b == 0:
    # Salida
    print("La ecuación tiene infinitas soluciones")
else:
    # Salida
    print("La ecuación no tiene solución")
