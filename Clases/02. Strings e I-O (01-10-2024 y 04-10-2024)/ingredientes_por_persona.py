# CONSTANTES
huevos_por_queque = 4
tazas_harina_por_queque = 8
tazas_leche_por_queque = 1/2
porciones_por_persona = 2
porciones_por_queque = 10

# ENTRADAS
numero_de_asistentes = input('Ingrese la cantidad de asistentes: ')

# PROCESAMIENTO
# Cambio la cantidad de asistentes de string a entero
numero_de_asistentes = int(numero_de_asistentes)
# Hago los cálculos por persona
huevos_por_persona = huevos_por_queque / porciones_por_queque
tazas_harina_por_persona = tazas_harina_por_queque / porciones_por_queque
tazas_leche_por_persona = tazas_leche_por_queque / porciones_por_queque
# Hago los cálculos por asistente
huevos_requeridos = huevos_por_persona * numero_de_asistentes * porciones_por_persona
tazas_de_harina_requeridas = tazas_harina_por_persona * numero_de_asistentes * porciones_por_persona
tazas_leche_por_requeridas = tazas_leche_por_persona * numero_de_asistentes * porciones_por_persona

# SALIDA
print('Se necesitan:', huevos_requeridos, 'huevos')
print('Se necesitan:', tazas_de_harina_requeridas, 'tazas de harina')
print('Se necesitan:', tazas_leche_por_requeridas, 'tazas de leche')

