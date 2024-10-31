# ENTRADA
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# PROCESAMIENTO
secuencia_buscada = "TATAAA" # TATAAAAAA
secuencia_salida = ""

while secuencia_buscada in secuencia_adn:
    secuencia_salida = secuencia_buscada
    secuencia_buscada = secuencia_buscada + "AAA" 
#  SALIDA 
if len(secuencia_salida)> 0:
    print("Se encontro la caja TATA:", secuencia_salida)
else:
    print("No se encontro la caja TATA")
