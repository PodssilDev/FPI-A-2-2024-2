'''
Para este ejercicio se restringe trabajar con String.
Aqui entra una de las alternativas para obtener el invertido
de un numero. Primero se aplica el modulo del numero y 10 para
obtener el ultimo digito del numero. Luego, en una variable nueva
se multiplica el numero * 10 (para agregar un 0 extra) y luego se
agrega ese último digito. Luego, se aplica numero // 10 para eliminar
el ultimo digito obtenido. El proceso se repite hasta que el numero
original sea negativo, es decir, que no queden digitos por invertir.
'''

# ENTRADA
numero = int(input("Ingrese un numero entero positivo: "))

# PROCESAMIENTO
invertido = 0
while numero > 0:
    # Se obtiene el ultimo digito del numero
    digito = numero % 10
    # Se agrega el digito al numero invertido
    
    invertido = invertido * 10 + digito
    # Se elimina el ultimo digito del numero original
    numero = numero // 10
    
# SALIDA
print("El numero invertido es:", invertido)
