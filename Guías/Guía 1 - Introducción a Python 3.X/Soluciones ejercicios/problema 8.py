# Programa que calcula el promedio y la desviación estándar de cuatro edades

#ENTRADAS
# Se solicita el ingreso de las edades 
edad_uno = int(input("Ingrese la edad de la primera persona: "))
edad_dos = int(input("Ingrese la edad de la segunda persona: "))
edad_tres = int(input("Ingrese la edad de la tercera persona: "))
edad_cuatro = int(input("Ingrese la edad de la cuarta persona: "))

#PROCESAMIENTO
# Calculo de el promedio de las edades
promedio = (edad_uno + edad_dos + edad_tres + edad_cuatro) / 4
# Calculo de la desviación estándar
desviacion_estandar = (((edad_uno - promedio) ** 2 + (edad_dos - promedio) ** 2
                        + (edad_tres - promedio) ** 2 + (edad_cuatro - promedio) ** 2) / 4) ** 0.5

#SALIDAS
# Muestar el proemedio 
print("El promedio de las edades es: ", promedio)
# Muestra la desviación estándar
print("La desviación estándar de las edades es: ", desviacion_estandar)
