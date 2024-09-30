# Programa que entrega la edad de acuerdo al anio actual
# CONSTANTES
# Se define el anio actual (2024)
ANIO_ACTUAL = 2024

# ENTRADAS
# Se solicita el ingreso del anio de nacimiento
anio_nacimiento = int(input("Ingrese el anio de nacimiento: "))

# PROCESAMIENTO
# Calcula la edad
edad = ANIO_ACTUAL - anio_nacimiento

# SALIDAS
# Entrega la edad
print("Usted tiene:", edad, "años")