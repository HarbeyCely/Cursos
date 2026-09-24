n = int(input("Ingrese un numero: "))
i = 0
facto = 1
while i < n:
    i += 1
    facto = facto * i
    print(facto)
print(f"El factorial de {n} es {facto}")