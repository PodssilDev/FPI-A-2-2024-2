# CONSTANTES
PRECIO_POR_KILOMETRO_A = 2.0
PRECIO_POR_KILOMETRO_B = 2.5
PRECIO_POR_KILOMETRO_C = 3.0
MINIMO_PERSONAS = 20

# ENTRADAS
personas = int(input("Ingrese una cantidad de personas: "))
kilometros = float(input("Ingrese el numero de kilometros a recorrer: "))
tipo_autobus = input("Ingrese el tipo de autobus (Puede ser A, B o C): ")

# PROCESAMIENTO
# Se ajuta el numero de personas si es menor al minimo
if personas < MINIMO_PERSONAS:
    personas = MINIMO_PERSONAS

# Se calcula el precio por tipo de autobus
if tipo_autobus == 'A':
    precio_por_kilometro = PRECIO_POR_KILOMETRO_A
elif tipo_autobus == 'B':
    precio_por_kilometro = PRECIO_POR_KILOMETRO_B
elif tipo_autobus == 'C':
    precio_por_kilometro = PRECIO_POR_KILOMETRO_C

# Se calcula el costo total
costo_total = personas * kilometros * precio_por_kilometro

# Se calcula el costo por persona
costo_por_persona = costo_total / personas

# SALIDAS
print("Costo total del viaje: $", costo_total)
print("Costo por persona: $", costo_por_persona)
