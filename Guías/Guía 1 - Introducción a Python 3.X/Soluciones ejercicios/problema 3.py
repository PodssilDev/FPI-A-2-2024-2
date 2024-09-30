# Programa que convierte dias a segundos
# CONSTANTES
HORAS_DIA = 24
SEGUNDOS_HORA = 3600

# DATOS DE ENTRADA 
# Se solicita el numero de dias a convertir
dias = int(input("Ingrese el numero de dias: "))

# PROCESAMIENTO
# Calcular el total de segundos 
segundos = dias * HORAS_DIA * SEGUNDOS_HORA

# SALIDA
# Entrega el total de segundos
print(dias, "dias equivalen a:", segundos, "segundos.") 
