# Calcula los primeros n terminos de una serie

# ENTRADA
# Solicita un numero
numero = int(input("Ingrese el numero de terminos de la serie: "))

# PROCESAMIENTO
# Inicializa la variable iteradora
k = 1
# Inicializa la variable acumuladora
suma = 0

while k <= numero:
    # Calcula los resultados parciales
    suma = suma + ((k ** 2 + 2)/(k ** 3 + 6 * k))
    # Incremeta el iterador
    k = k + 1

# SALIDA
print("La suma de los primeros", numero, "terminos de la serie es: ", suma)
