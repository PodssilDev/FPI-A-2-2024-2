# Obtener el promedio semestral de un estudiante

# ENTRADAS
nombre = input("Introduce tu nombre: ")
tarea_1 = float(input("Introduce la nota de Tarea 1 (10%): "))
tarea_2 = float(input("Introduce la nota de Tarea 2 (20%): "))
tarea_3 = float(input("Introduce la nota de Tarea 3 (30%): "))
controles = float(input("Introduce la nota de Controles (15%): "))
guias = float(input("Introduce la nota de Guías (25%): "))

# PROCESAMIENTO
# Calcular el promedio ponderado
promedio = (tarea_1 * 0.10) + (tarea_2 * 0.20) + (tarea_3 * 0.30) + (controles * 0.15) + (guias * 0.25)

# SALIDA
# Se utiliza round para redondear el promedio a 2 decimales
print(nombre, "tu promedio semestral es:", round(promedio,2))