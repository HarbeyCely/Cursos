
n = int(input("Introduce un numero entero positivo mayor que 2: "))
i = 2
while (n % i != 0) and n > 1:
    i += 1

if n <= 1:
    print("El numero ingresado no es valido.")
elif i == n:
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")