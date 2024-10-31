# Determina si una palabra es palindromo

# ENTRADA
palabra = input('Ingrese una palabra: ')

# PROCESAMIENTO
palabra = palabra.lower()
palabra_invertida = "" 

i = 0
while i < len(palabra):
    palabra_invertida = palabra[i] + palabra_invertida 
    i = i + 1

# SALIDA
if palabra == palabra_invertida: 
    print("La palabra",palabra,"es palindromo") 
else: 
    print(palabra,"no es palíndromo")
