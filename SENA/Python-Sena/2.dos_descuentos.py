# PROGRAMA SI EL PRECIO DE UN PRODUCTO ES MAYOR O IGUAL A 500.000 OBTENDRA DESCUENTO DEL 20%
# DE LO CONTRARIO EL DESCUENTO ES DE 5%

precio_producto = float(input("Ingrese el precio del producto: "))
if (precio_producto >= 500000):
    precio_final = precio_producto * (1-0.2)
    print(f"El precio inicial fue {precio_producto} y el precio final es {precio_final}")
else:
    precio_final = precio_producto * (1-0.05)
    print(f"El precio inicial fue {precio_producto} y el precio final es {precio_final}")