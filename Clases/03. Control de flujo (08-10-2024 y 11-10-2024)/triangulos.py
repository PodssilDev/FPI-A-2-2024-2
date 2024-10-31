# ENTRADA
angulo1 = int(input("Ingresa el valor del primer angulo: "))
angulo2 = int(input("Ingresa el valor del segundo angulo: "))

# PROCESAMIENTO Y SALIDAS

# Se calcula el tercer angulo
angulo3 = 180 - (angulo1 + angulo2)

# Se verifica si los angulos son validos
if angulo1 <= 0 or angulo2 <= 0 or angulo3 <= 0:
    print("Los angulos no son validos.")
else:
    # Clasificacion del triángulo
    if angulo1 == angulo2 == angulo3:
        print("El triangulo es equilatero")
    elif angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")
