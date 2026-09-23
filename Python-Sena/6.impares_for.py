# PROGRAMA PARA QUE MUESTRE LOS NUMEROS IMPARES ENTRE 1 Y NUMERO

num = int(input("Ingresa numero: "))
for i in range(1,num):
    if (i % 2 != 0):
        print("Numero impares",i)
        