arreglo = [
    [10, 20, 30],
    [5, 10, 15],
    [1, 2, 3]
]
# PARA MOSTRAR LA MATRIZ VACIA POR COLUMNAS
for i in arreglo:
    print(i[0], end="\t")
    print(i[1], end="\t")
    print(i[2])
# PARA MOSTRAR LA MATRIZ VACIA POR FILAS
for i in arreglo[0]:
    print(i, end="\t")
print("\n")
for i in arreglo[1]:
    print(i, end="\t")
print("\n")
for i in arreglo[2]:
    print(i, end="\t")