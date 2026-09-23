# PROGRAMA PARA CREAR CUALQUIER TABLA DE MULTIPLICARA

num = int(input("Ingrese el número de la tabla que desea: "))
for i in range(11):
    valor = num * i
    print(f"{num} x {i} = {valor}")