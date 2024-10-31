print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Salir")
opcion = int(input("Ingresa una opcion: "))
while opcion != 5:
    num1 = int(input("Ingresame un numero: "))
    num2 = int(input("Ingresame otro numero: "))
    resultado = 0
    if opcion == 1:
        resultado = num1 + num2
        print(resultado)
    elif opcion == 2:
        resultado = num1 - num2
        print(resultado)
    elif opcion == 3:
        resultado = num1 * num2
        print(resultado)
    elif opcion == 4:
        resultado = num1 // num2
        print(resultado)
    else:
        print("Usted es weon")
    print()
    
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opcion = int(input("Ingresa una opcion: "))
