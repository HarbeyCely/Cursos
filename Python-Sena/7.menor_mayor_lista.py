# ESCRIBIR UN PROGRAMA QUE ALMACENE EN UNA LISTA PRECIOS, MOSTRAR MENOR Y MAYOR

precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for n in precios:
    if n < min:
        min = n
    elif n > max:
        max = n
print("El minimo es ",min)
print("El maximo es ",max)