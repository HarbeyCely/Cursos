# QUE PIDA UN NUMERO ENTERO Y MUESTRE POR PANTALLA SI ES PAR O IMPAR
n = int(input("Ingrese un numero entero: "))
if (n % 2 != 0):
    print("El numero " + str(n) + " es Impar.")
else:
    print("El numero " + str(n) + " es Par.")

# str() convierte el parametro en texto y el operador + concatena cadenas