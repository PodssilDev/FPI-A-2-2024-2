# Programa que calcula el numero aproximado de atomos de una 
# persona y el porcentaje del universo que ellos representan

# CONSTANTES
ATOMOS_UNIVERSO = 10 ** 81
PESO_PROMEDIO = 70
ATOMOS_PROMEDIO = 7 * 10 ** 27

# ENTRADAS
# Se solicita el peso de la persona
peso = float(input("Ingrese su peso en kilogramos: "))

# PROCESAMIENTO
# Calcula el numero de atomos en la persona
numero_de_atomos = (peso / PESO_PROMEDIO) * ATOMOS_PROMEDIO
# Calcula el porcentaje de atomos en el universo
porcentaje_atomos = (numero_de_atomos / ATOMOS_UNIVERSO) * 100

# SALIDAS
print("El numero de atomos en su cuerpo es:", numero_de_atomos)
print("Sus atomos son un", porcentaje_atomos, "% del universo") 
