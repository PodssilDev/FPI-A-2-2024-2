# Verifica que los parentesis de una expresion se encuentren
# correctamente pareados

# ENTRADA
expresion = input("Ingrese una expresion: ")
 
# PROCESAMIENTO
parentesis_izquierdo = 0
parentesis_derecho = 0
i = 0
while i < len(expresion):
    if expresion[i] == ")": 
        if parentesis_izquierdo > 0:
            parentesis_izquierdo = parentesis_izquierdo - 1
        else:
            parentesis_derecho = parentesis_derecho + 1            
    else:
        if expresion[i] == "(": 
            parentesis_izquierdo = parentesis_izquierdo + 1
    i = i + 1

# SALIDA
if parentesis_izquierdo == 0 and parentesis_derecho == 0:
    print("La expresion es correcta")
if parentesis_izquierdo != 0:
    print("La expresion contiene",parentesis_izquierdo,"parentesis sin cerrar")
if parentesis_derecho != 0:
    print("La expresion contiene",parentesis_derecho,"parentesis sin abrir")
