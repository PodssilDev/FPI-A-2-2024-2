# ENTRADA
valor_compra = float(input("Ingrese el valor de la compra: "))

# PROCESAMIENTO
# Asigna el descuento para compras menores o iguales a 30000
if valor_compra <= 30000:
    # Asigna el descuento
    descuento = 0
# Asigna el descuento para compras entre 30000 y 80000
elif valor_compra <= 80000:
    descuento = 0.08
# Asigna el descuento para compras entre 80000 y 150000
elif valor_compra <= 150000:
    descuento = 0.12
# Asigna el descuento para compras entre 150000 y 250000
elif valor_compra <= 250000:
    descuento = 0.15
else:
    # Asigna el descuento para compras mayores a 250000
    descuento = 0.18
# Calcula el valor del descuento
valor_descuento = valor_compra * descuento
# Calcula el valor final de la compra
valor_final = valor_compra - valor_descuento

# SALIDA
# Informa los valores
print("El valor del descuento es", valor_descuento, "y el valor final es", valor_final)
