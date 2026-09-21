# VERIFICAR SI ES TRIANGULO EQUILATERO
angulo1 = float(input("Ingrese el angulo 1 en grados "))
angulo2 = float(input("Ingrese el angulo 2 en grados "))
angulo3 = 180 - angulo1 - angulo2

if (angulo1 == angulo2 and angulo2 == angulo3):
    print("Es triangulo equilatero")
else:
    print("Es un triangulo normal")