# ENTRADAS
anio = int(input("Ingresa el anio: "))
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el dia: "))

# PROCESAMIENTO
# Se verifica si el anio es bisiesto
bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
# Se verifica si la fecha es valida
if mes < 1 or mes > 12:
    print("Fecha no valida: el mes debe estar entre 1 y 12")
elif dia < 1:
    print("Fecha no valida: el dia debe ser mayor a 0")
else:
    # SALIDAS
    # Se verifica cada mes y los dias asociados
    if mes == 1:  # Enero
        if dia <= 31:
            print("La fecha es valida")
        else:
            print("Fecha no valida: enero tiene 31 dias")
    elif mes == 2:  # Febrero
        if bisiesto and dia <= 29:
            print("La fecha es valida")
        elif not bisiesto and dia <= 28:
            print("La fecha es valida")
        else:
            print("Fecha no valida: febrero tiene 29 dias en anios bisiestos o 28 dias")
    elif mes == 3:  # Marzo
        if dia <= 31:
            print("La fecha es valida")
        else:
            print("Fecha no valida: marzo tiene 31 dias")
    elif mes == 4:  # Abril
        if dia <= 30:
            print("La fecha es valida")
        else:
            print("Fecha no valida: abril tiene 30 dias")
    elif mes == 5:  # Mayo
        if dia <= 31:
            print("La fecha es valida")
        else:
            print("Fecha no valida: mayo tiene 31 dias")
    elif mes == 6:  # Junio
        if dia <= 30:
            print("La fecha es valida")
        else:
            print("Fecha no valida: junio tiene 30 dias")
    elif mes == 7:  # Julio
        if dia <= 31:
            print("La fecha es valida")
        else:
            print("Fecha no valida: julio tiene 31 dias")
    elif mes == 8:  # Agosto
        if dia <= 31:
            print("La fecha es valida.")
        else:
            print("Fecha no valida: agosto tiene 31 dias")
    elif mes == 9:  # Septiembre
        if dia <= 30:
            print("La fecha es valida")
        else:
            print("Fecha no valida: septiembre tiene 30 dias")
    elif mes == 10:  # Octubre
        if dia <= 31:
            print("La fecha es valida")
        else:
            print("Fecha no valida: octubre tiene 31 dias")
    elif mes == 11:  # Noviembre
        if dia <= 30:
            print("La fecha es valida")
        else:
            print("Fecha no valida: noviembre tiene 30 dias")
    elif mes == 12:  # Diciembre
        if dia <= 31:
            print("La fecha es valida.")
        else:
            print("Fecha no valida: diciembre tiene 31 dias")
