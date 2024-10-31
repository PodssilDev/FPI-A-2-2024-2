# Numero de vocales en una oracion

# ENTRADAS
oracion = input("Ingrese una oracion: ")

# PROCESAMIENTO
# Se calcula el numero de vocales (Usando count)
numero_de_vocales = 0
numero_de_vocales += oracion.count('a')
numero_de_vocales += oracion.count('e')
numero_de_vocales += oracion.count('i')
numero_de_vocales += oracion.count('o')
numero_de_vocales += oracion.count('u')
numero_de_vocales += oracion.count('A')
numero_de_vocales += oracion.count('E')
numero_de_vocales += oracion.count('I')
numero_de_vocales += oracion.count('O')
numero_de_vocales += oracion.count('U')

# SALIDA
print("El numero de vocales en la oracion es:", numero_de_vocales)