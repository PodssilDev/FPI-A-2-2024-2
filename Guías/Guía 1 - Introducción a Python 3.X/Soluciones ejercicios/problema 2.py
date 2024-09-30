# Calcula el area de un triangulo mediante la formula de Heron
# ENTRADAS
# Se solicita el ingreso de los lados
a = float(input("ingrese el valor de uno de los lados del triangulo: "))
b = float(input("ingrese el valor de otro de los lados: "))
c = float(input("ingrese el valor del lado restante: "))

# PROCESAMIENTO 
# Calcula el semiperimetro
semi = (a + b + c) / 2
# Calcula el area
area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5

# SALIDAS
# Entrega el area y los lados
print("El valor del area del triingulo de lados", a, b, c, "es :", area) 

