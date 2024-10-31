# Multiplica dos numeros enteros positivos mediante sumas sucesivas
# ENTRADAS
# Solicita un numero
multiplicando = int(input("Ingrese un multiplicando: "))
# Solicita otro numero
multiplicador = int(input("Ingrese un multiplicador: "))

# PROCESAMIENTO
# Inicializa una variable acumuladora 
producto = 0
# Inicializa una variable iteradora
i = 0
# Calcula la multiplicacion mediante sumas
while i < multiplicador:
    # Acumula los resultados parciales
    producto = producto + multiplicando
    # Incrementa la variable iteradora
    i = i + 1

# SALIDA
print("El resultado de multiplicar", multiplicando, "por", multiplicador, "es:", producto) 
