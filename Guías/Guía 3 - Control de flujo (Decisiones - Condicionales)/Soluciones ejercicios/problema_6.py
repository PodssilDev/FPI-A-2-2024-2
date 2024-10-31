# ENTRADAS
# Solicita ingresar el tipo de uva 
tipo_de_uva = input("Ingrese el tipo de uva A o B: ")
# Solicita ingresar el tamanio de uva 
tamano_de_uva = input("Ingrese el tamanio de uva 1 o 2: ")
# Solicita ingresar el numero de kilos  
kilos = float(input("Ingrese el numero de kilos: "))
# Solicita ingresar el precio por kilo 
precio = float(input("Ingrese precio por kilo en pesos: "))

# PROCESAMIENTO
# Determina si el tipo de uva ingresado es A o B
if tipo_de_uva == "A":
    # Determina si el tamanio de uva ingresado es 1 o 2
    if tamano_de_uva == "1":
        # Calcula el precio para uva tipo A y tamanio 1
        precio = precio + 20
    else:
        # Calcula el precio para uva tipo A y tamanio 2
        precio = precio + 30
# Se ejecuta cuando el tipo de uva es B
else:
    if tamano_de_uva == "1":
        # Calcula el precio para uva tipo B y tamanio 1
        precio = precio - 30
    else:
        # Calcula el precio para uva tipo B y tamanio 2
        precio = precio - 50
# Calcula el ingreso total 
ingreso = precio * kilos

# SALIDA
print("El ingreso total es:", ingreso)
