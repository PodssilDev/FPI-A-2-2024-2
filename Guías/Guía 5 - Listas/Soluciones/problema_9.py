# ENTRADA 
cantidad_sublistas = int(input("Ingrese la cantidad de sub-listas: "))
i = 0
lista_maestra = []
while i < cantidad_sublistas:
    numeros = input("Ingrese numeros separados por coma (,) para la sub-lista " + str(i+1) + " : ")
    lista_numeros = numeros.split(",")
    largo_lista = len(lista_numeros)
    for posicion in range(0, largo_lista):
        lista_numeros[posicion] = int(lista_numeros[posicion])
    lista_maestra.append(lista_numeros)
    i += 1

# PROCESAMIENTO
lista_promedios = []
for lista in lista_maestra:
    promedio = (sum(lista) / len(lista))
    lista_promedios.append(promedio)

mayor_promedio = max(lista_promedios)
i = 0

# SALIDA
while i < len(lista_promedios):
    
    if mayor_promedio == lista_promedios[i]:
        print("La posicion de la sub-lista con el mayor promedio es:", i)
    i += 1
