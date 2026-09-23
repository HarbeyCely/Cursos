lista = [1,2,3,4,5,8,9]
numero = int(input("Ingrese un numero: "))
encontrado = bool()
for n in lista:
    if n == numero:
        encontrado = True
        break
        
if encontrado:
    print("SI se encontro el numero")
else:
    print("NO se encontro el numero")