# Programa que calcula el valor final de un credito con interes
# compuesto y el valor de la cuota

# ENTRADAS
# Solicita el valor inicial del credito
valor_inicial=  float(input("Ingrese el valor del credito: "))
# Solicita la tasa de interes
tasa_interes = float(input("Ingrese el valor de la tasa de interes: "))
# Solicita la cantidad de cuotas
numero_cuotas = int(input("Ingrese el numero de cuotas: "))

# PROCESAMIENTO
# Calcula el valor final del credito
valor_final = int(valor_inicial * (1 + (tasa_interes / 100)) ** numero_cuotas)
# Calcula el valor de la cuota
valor_cuotas = int(valor_final / numero_cuotas)

# SALIDA
print("El valor final del credito es: ", valor_final, "pesos")
print("El valor de cada cuota es : ", valor_cuotas, "pesos")
