# Calcula la relación lineal entre grados Fahrenheit y grados Celsius 
# CONSTANTES
# Abscisa del punto uno 
PUNTO_UNO_X = 32
# Ordenada del punto dos 
PUNTO_UNO_Y = 0
# Abscisa del punto uno 
PUNTO_DOS_X = 50
# Ordenada del punto dos
PUNTO_DOS_Y = 10

# PROCESAMIENTO
# Calcula la pendiente
m = (PUNTO_DOS_Y - PUNTO_UNO_Y) / (PUNTO_DOS_X - PUNTO_UNO_X)
# Calcula la ordenada al origen
b = PUNTO_UNO_Y - m * PUNTO_UNO_X

# SALIDAS
# Entrega el valor de la pendiente
print("La pendiente de la ecuación es: ",m)
# Entrega el valor de la ordenada al origen
print("La ordenada al origen es: ",b)
