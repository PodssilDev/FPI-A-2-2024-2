# Calcula el cuadrado de un numero mediante sumas sucesivas
# ENTRADA
# Solicita un numero
numero = int(input("Ingrese un numero: "))

# PROCESAMIENTO
# Calcula el valor absoluto 
if numero < 0:
    numero_absoluto = -numero
else:
    numero_absoluto = numero
# Inicializa la variable acumuladora
resultado = 0
# Inicializa la variable iteradora
i = 1
# Calcula el cuadrado mediante sumas
while (i <= numero_absoluto):
    # Acumula los resultados parciales
    resultado = resultado + numero_absoluto
    # Incrementa la variable iteradora
    i = i + 1

#SALIDA
print("El cuadrado del numero", numero, "es:", resultado)
