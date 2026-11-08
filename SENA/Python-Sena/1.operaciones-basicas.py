# Programa que haga las operaciones basicas y que las muestre
numero_inicial = float(input("Ingrese un numero: "))
numero_secundario = float(input("Ingrese otro numero: "))

suma = numero_inicial + numero_secundario
resta = numero_inicial - numero_secundario
multiplicacion = numero_inicial * numero_secundario
division = numero_inicial / numero_secundario

print(f"\nSuma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {round(division,2)}")
