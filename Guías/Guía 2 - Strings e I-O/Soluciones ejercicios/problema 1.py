# Solicita anio actual, anio de nacimiento y nombre,
# calcula la cantidad de minutos que has vivido, el numero
# minimo y maximo de respiraciones y el numero de latidos


# CONSTANTES
RESPIRACIONES_POR_MINUTO_MIN = 12
RESPIRACIONES_POR_MINUTO_MAX = 20
LATIDOS_POR_MINUTO = 67.5

# ENTRADAS
anio_actual = int(input("Introduce el anio actual: "))
nombre = input("Introduce tu nombre: ")
anio_nacimiento = int(input("Introduce tu año de nacimiento: "))

# PROCESAMIENTO
# Se calcula la edad
edad = anio_actual - anio_nacimiento

# Se calcula la cantidad de minutos que se ha vivido
minutos_por_anio = 365 * 24 * 60
minutos_totales = edad * minutos_por_anio

# Se calcula el numero minimo y maximo de respiraciones
numero_minimo_de_respiraciones = minutos_totales * RESPIRACIONES_POR_MINUTO_MIN
numero_maximo_de_respiraciones = minutos_totales * RESPIRACIONES_POR_MINUTO_MAX

# Se calcular el numero de latidos
numero_de_latidos = minutos_totales * LATIDOS_POR_MINUTO

# SALIDA
print("Hola", nombre, "naciste el año", anio_nacimiento, "y tu edad es", edad,
      "años. Durante tu vida has respirado entre", numero_minimo_de_respiraciones,
      "veces y", numero_maximo_de_respiraciones, "veces. Tu corazón ha latido",
      numero_de_latidos, "veces.")
