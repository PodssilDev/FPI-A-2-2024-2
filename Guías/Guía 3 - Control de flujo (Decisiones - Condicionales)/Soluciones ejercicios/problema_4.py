# ENTRADAS
a = float(input("Ingrese el valor del coeficiente a: "))
b = float(input("Ingrese el valor del coeficiente b: "))

# PROCESAMIENTO
# Determina si coeficiente a es distinto a cero
if a != 0:
    solucion = -b / a
    # SALIDA
    print("La solución de la ecuacion es: ", solucion)
# Determina si coeficiente b es igual a cero
elif b == 0:
    # SALIDA
    print("La ecuacion tiene infinitas soluciones")
else:
    # SALIDA
    print("La ecuacion no tiene solución")
