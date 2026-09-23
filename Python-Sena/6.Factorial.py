# PROGRAMA PARA CALCULAR EL FACTORIAL DE 5
n = int(input("Ingrese el numero del que desea el factorial: "))
i = 0
facto = 1
for n in range(n):
    i += 1
    facto = facto * i
    print(facto)
print(f"El resultado de {n+1}! es {facto}")