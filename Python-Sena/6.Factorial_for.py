# PROGRAMA PARA CALCULAR EL FACTORIAL DE 5
n = int(input("Ingrese el numero del que desea el factorial: "))
i = 0
factorial = 1
for n in range(n):
    i += 1
    factorial = factorial * i
    print(factorial)
print(f"El resultado de {n+1}! es {factorial}")