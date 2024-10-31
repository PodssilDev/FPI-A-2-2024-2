# ENTRADA
cantidad = int(input("Ingresa la cantidad de dinero: "))

# PROCESAMIENTO
# Billetes y monedas
billetes_20000 = cantidad // 20000
cantidad = cantidad % 20000

billetes_10000 = cantidad // 10000
cantidad = cantidad % 10000

billetes_5000 = cantidad // 5000
cantidad = cantidad % 5000

billetes_2000 = cantidad // 2000
cantidad = cantidad % 2000

billetes_1000 = cantidad // 1000
cantidad = cantidad % 1000

monedas_500 = cantidad // 500
cantidad = cantidad % 500

monedas_100 = cantidad // 100
cantidad = cantidad % 100

monedas_50 = cantidad // 50
cantidad = cantidad % 50

monedas_10 = cantidad // 10
cantidad = cantidad % 10

monedas_5 = cantidad // 5
cantidad = cantidad % 5

monedas_1 = cantidad // 1

# SALIDAS
if billetes_20000 > 0:
    print(billetes_20000, "billete(s) de $20.000")
if billetes_10000 > 0:
    print(billetes_10000, "billete(s) de $10.000")
if billetes_5000 > 0:
    print(billetes_5000, "billete(s) de $5.000")
if billetes_2000 > 0:
    print(billetes_2000, "billete(s) de $2.000")
if billetes_1000 > 0:
    print(billetes_1000, "billete(s) de $1.000")
if monedas_500 > 0:
    print(monedas_500, "moneda(s) de $500")
if monedas_100 > 0:
    print(monedas_100, "moneda(s) de $100")
if monedas_50 > 0:
    print(monedas_50, "moneda(s) de $50")
if monedas_10 > 0:
    print(monedas_10, "moneda(s) de $10")
if monedas_5 > 0:
    print(monedas_5, "moneda(s) de $5")
if monedas_1 > 0:
    print(monedas_1, "moneda(s) de $1")
