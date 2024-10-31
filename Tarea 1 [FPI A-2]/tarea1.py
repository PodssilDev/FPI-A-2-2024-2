# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA 
# AYUDANTÍA 1 - RESOLUCIÓN TAREA 1 

# CONSTANTES

# ENTRADAS
numero = int(input("Ingrese un numero palindromico: "))

# Verifica que la entrada sea un numero positivo
while numero <= 0:
    print("Error: Debe ingresar un número entero positivo palindrómico.")
    numero = int(input("Ingrese un numero palindromico:"))

# PROCESAMIENTO
# Convierte el numero en string
numero_str = str(numero)
# Invierte el número
numero_invertido = numero_str[::-1]
# Contador de pasos
pasos = 0

while numero_str != numero_invertido:
    if pasos > 0:
        print("Intermedio:", numero)
    # Sumar el numero invertido al numero original
    numero = numero + int(numero_invertido)
    # Convertir el numero a string
    numero_str = str(numero)
    # Invertimos el numero
    numero_invertido = numero_str[::-1]
    # Aumentar el contador de pasos
    pasos = pasos + 1


# SALIDAS
print("Generado en", pasos, "pasos")
print("Palindromo final:", numero)
    
    
