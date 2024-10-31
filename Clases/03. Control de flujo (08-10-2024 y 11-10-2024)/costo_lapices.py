# ENTRADAS
# Solicita el número de lápices
numero_lapices = int(input("Ingrese el número de lápices: ")) 
# PROCESAMIENTO
# Determina si el número ingresado es mayor o igual a 1000 
if numero_lapices >= 1000:
    # Calcula el costo total con precio de 850
    costo_total = numero_lapices * 850
else:
    # Calcula el costo total con precio de 900
    costo_total = numero_lapices * 900
# SALIDAS
print("Se debe pagar un total de", costo_total)
