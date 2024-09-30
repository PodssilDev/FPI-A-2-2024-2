# Programa que convierte segundos a horas, minutos y segundos
# CONSTANTES
SEGUNDOS_HORA = 3600
SEGUNDOS_MINUTO = 60

# DATOS DE ENTRADA
# Se solicita el numero de segundos a convertir
segundos_ingresados = int(input("Ingrese el numero de segundos: "))

# PROCESAMIENTO
# Calcular el total de horas 
horas = segundos_ingresados // SEGUNDOS_HORA
# Calcular el total de minutos
minutos = (segundos_ingresados % SEGUNDOS_HORA) // SEGUNDOS_MINUTO
# Calcular el total de segundos
segundos = (segundos_ingresados % SEGUNDOS_HORA) % SEGUNDOS_MINUTO 

# SALIDA
# Entrega el resultado
print(segundos_ingresados, "segundos equivalen a:", horas, "horas", minutos,
      "minutos", segundos, "segundos") 
