# Programa para calcular el IVA de un articulo si su precio es >= 100.000
compra = float(input("Ingrese valor de la compra: "))
if compra >= 100000:
    iva = compra * 0.19
    print("El Iva es: ",iva)
    total = compra+iva
    print("El total es",total)
else:
    print("No paga Iva")
