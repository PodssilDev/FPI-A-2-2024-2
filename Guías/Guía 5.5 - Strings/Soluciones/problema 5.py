# ENTRADA
texto = input("Ingrese un texto: ")

# PROCESAMIENTO
texto_nuevo = texto[0]
i = 1
while i < len(texto):
    if texto[i] == texto[0]:
        texto_nuevo = texto_nuevo + "$"
    else:
        texto_nuevo = texto_nuevo + texto[i]
    i = i + 1

# SALIDA
print('Cadena con remplazo:', texto_nuevo)
