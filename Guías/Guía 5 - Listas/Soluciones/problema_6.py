# ENTRADA
numeros = input("Ingrese varios numeros separados por coma (,): ")

# PROCESAMIENTO
# Se crea la lista de numeros y se transforman de string a int
lista_numeros = numeros.split(",")
for posicion in range(0,len(lista_numeros)):
    lista_numeros[posicion] = int(lista_numeros[posicion])
# Se declara la variable donde se guardara el maximo impar
max_impar = -1
# Se recorre la lista de numeros
for i in range(len(lista_numeros)):
    # Se comprueba si el numero es impar y mayor que el
    # maximo impar actual
    if lista_numeros[i] % 2 != 0:
        if lista_numeros[i] > max_impar:
            max_impar = lista_numeros[i]

# SALIDA
if max_impar == -1:
    print("No existen numeros impares.")
else:
    print("El numero impar mas grande ingresado es:", max_impar)

