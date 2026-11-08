# QUE PIDA UN NUMERO ENTERO Y MUESTRE POR PANTALLA SI ES PAR O IMPAR
n = int(input("Ingrese un numero entero: "))
if (n % 2 == 0):
    print("El numero " + str(n) + " es par.")
else:
    print("El numero " + str(n) + " es impar.")

# str() convierte el parametro en texto y el operador + concatena cadenas