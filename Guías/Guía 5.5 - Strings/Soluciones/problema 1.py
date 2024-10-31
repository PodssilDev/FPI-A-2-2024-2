# Cuenta el numero total de vocales en un texto
# ENTRADA
texto = input("Ingrese un texto: ")

# PROCESAMIENTO
contador_vocales = 0
texto = texto.lower()
i = 0
while i < len(texto):
    if texto[i] in "aeiou":
        contador_vocales = contador_vocales + 1
    i = i + 1
 
# SALIDA
print("Se contaron",contador_vocales,"vocales en el texto")
    
