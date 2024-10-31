# ENTRADAS
# Solicita el numero de lapices
numero_lapices = int(input("Ingrese el numero de lapices: "))
# PROCESAMIENTO
# Determina si el numero ingresado es mayor o igual a 1000
if numero_lapices >= 1000:
    # Calcula el costo total con precio de 850
    costo_total = numero_lapices * 850
else:
    # Calcula el costo total con precio de 900 
    costo_total = numero_lapices * 900
# SALIDA
print("Se debe pagar un total de", costo_total, "por", numero_lapices, "lapices")
