# DATOS ENTRADA
a = float(input("Ingrese el valor del coeficiente a: "))
b = float(input("Ingrese el valor del coeficiente b: "))
c = float(input("Ingrese el valor del coeficiente c: "))

# PROCESAMIENTO
if a != 0:
    discriminante = b ** 2.0 - 4.0 * a * c
    if discriminante > 0:
        x1 = (-b + discriminante ** 0.5) / (2.0 * a)
        x2 = (-b - discriminante ** 0.5) / (2.0 * a)
        print("Las soluciones de la ecuacion son :", x1, "y", x2)
    elif  discriminante == 0:
        x1 = (-b) / (2.0 * a)
        print("La ecuacion tiene solucion unica :", x1)
    else:
        print("La ecuacion no tiene solucion")
else:
    print("No es una ecuacion de segundo grado")
