# ENTRADA
numero_minutos = float(input("Ingrese el numero de minutos de permanencia: "))

# PROCESAMIENTO

if numero_minutos <= 30:
    tarifa = numero_minutos * 35
elif numero_minutos <= 120:
    tarifa = (30 * 35) + (numero_minutos - 30) * 30
elif numero_minutos <= 240:
    tarifa = (30 * 35) + (90 * 30) + (numero_minutos - 120) * 25
else:
    tarifa = (30 * 35) + (90 * 30) + (120 * 25) + (numero_minutos - 240) * 20
tarifa = int(tarifa)

# SALIDA
print("El costo por el uso del estacionamiento es:",tarifa,"pesos")
