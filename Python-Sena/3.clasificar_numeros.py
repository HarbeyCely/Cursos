# CLASIFICAR NUMERO EN POSITIVO, NEGATIVO Y NEUTRO
numero = float(input("Ingrese un numero: "))
if (numero>0):
    print("El numero es positivo")
else:
    if (numero==0):
        print("El numero es cero")
    else:
        print("El numero es negativo")