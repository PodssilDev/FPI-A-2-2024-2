# Calcula los numeros de la sucesion de fibonacci menores que n 
# ENTRADA
# Solicita un numero
numero = int(input("Ingrese un numero entero mayor que cero: "))

#PROCESAMIENTO
# Inicializa el primer termino de la sucesion
f0 = 0
# Inicializa el segundo termino de la sucesion
f1 = 1
# Inicializa una variable auxiliar
auxiliar = 0
# Se imprime el primer termino de sucesion
print(f0)
# Mientras el termino actual sea menor que el numero ingresado  
while f1 < numero:
    # Imprime los terminos de la sucesión
    print(f1) 
    # Actualiza los terminos de la sucesion
    auxiliar = f0
    f0 = f1
    f1 = f1 + auxiliar



