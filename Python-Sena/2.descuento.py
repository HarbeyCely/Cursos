# SI EL PRECIO DE UN PRODUCTO ES MAYOR O IGUAL A 500.000 OBTENDRA UN DESCUENTO DEL 5%
precio_producto = float(input("Ingresa  el precio del producto: "))
if (precio_producto >= 500000):
    descuento = precio_producto * 0.05
    print("El descuento es $",descuento)
    pagofinal = precio_producto - descuento
    print("El pago final es $",pagofinal)
else:
    print("No tiene descuento")
