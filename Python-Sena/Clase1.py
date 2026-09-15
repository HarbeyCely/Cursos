# # Calcular area de un triangulo
# Area = float()
# # cual es la variable cadena y la variable lista " " ?
# base = int(input("Ingresa el valor de la base: "))
# altura = int(input("Ingresa el valor de la altura: "))
# area = (base * altura)/2
# print(f"El area es {area} m2")



# Programa para calcular el IVA de un articulo si su precio es >= 100.000
compra = float(input("Ingrese valor de la compra: "))
if compra >= 100000:
    iva = compra * 0.19
    print("El Iva es: ",iva)
    total = compra+iva
    print("El total es",total)
else:
    print("No paga Iva")
