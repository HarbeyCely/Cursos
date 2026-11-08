# PROGRAMA PARA PEDIR UN NUMERO, SUMARLO CON OTRO NUMERO SIGUIENTE Y SI SE DIGITA CERO SALIR
suma = 0
while True:
    numero = int(input("Ingrese un numero: (o escribe 0 para salir) "))
    if numero == 0:
        break
    suma += numero
    print("\nLa suma actual es ",suma)
print("-----------------------")
print("La suma total es ",suma)
print("-----------------------")
