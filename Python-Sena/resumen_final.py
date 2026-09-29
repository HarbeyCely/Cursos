# 1) Calcular el area de un triangulo

# b = float(input("Inserte la base del triangulo: "))
# h = float(input("Inserte la altura del triangulo: "))
# area = (b * h) / 2
# print("El area de ese triangulo es:",area)

# 2) Calcular el iva de una compra

# compra = float(input("Ingrese el valor de la compra: $"))
# if (compra >= 1200000):
#     iva = compra * 0.19
#     pago_final = compra + iva
# else:
#     pago_final = compra * (1 + 0.05)
# print(f"El valor del pago final es: ${pago_final}")

# 3) Practicas de deportes con Elif

# deporte = input("Que deporte practicas?: ").lower()
# if (deporte == "futbol"):
#     print("Ud practica futbol")
# elif (deporte == "karate"):
#     print("Ud practica karate")
# elif (deporte == "tenis"):
#     print("Ud practica tenis")
# elif (deporte == "rugby"):
#     print("Ud practica rugby")
# elif (deporte == "ping pong"):
#     print("Ud practica ping pong")
# else:
#     print("Ud practica un deporte diferente")

# 4) Programa para contar los numeros de 1 a 20

# orden = input("Como desea contar ascendente (a) o descendente (d): ")
# if orden == 'a':
#     for i in range(1,21):
#         print(i)
# elif orden == 'd':     
#     numero = 21
#     for i in range(1,numero):
#         numero -= 1
#         print(numero)
# else:
#     print("Opcion invalida")

# 5) Tablas

# num = int(input("Que tabla quiere hacer? Ingrese el numero: "))
# contador = 0
# while contador < 10:
#     contador += 1
#     result = num * contador
#     print(f"{num} X {contador} = {result}")

# 6) Factorial con while
# n = int(input("Ingrese un numero para calcular su factorial: "))
# num = n
# result = 1
# while n >= 2:
#     result = result * n
#     n -= 1
#     print(result)
# print(f"El factorial de {num} es {result}")


# 7) Lista
# balones = ["rojo", "blanco", "azul"]
# print(balones)
# balones.append("verde")
# print(balones)
# balones.remove("blanco")
# print(balones)
# balones.sort()
# print(balones)

# 8) Funcion

def suma(a,b):
    return a+b

print("El resultado de la suma es:",suma(2,4))

def resta(a,b):
    return a-b

print("El resultado de la resta es:",resta(6,4))

def multiplicar(a,b):
    return a*b

print("El resultado de la multiplicacion es:",multiplicar(2,4))