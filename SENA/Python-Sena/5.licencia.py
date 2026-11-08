# EJERCICIO ELIF CONDICIONAL, MOSTRAR TIPO DE LICENCIA AL QUE TIENE DERECHO POR EDAD
# 16 A 18 PERMISO DE LOS PADRES
# MAYOR O IGUAL A 18 AÑOS Y MENOR A 60 LICENCIA NORMAL
# ENTRE 60 Y 80 RENOVAR CADA 5 AÑOS Y MAS DE 80 CADA 1 AÑO
edad = int()
while edad != 1:
    edad = int(input("Ingrese la edad: "))
    if (edad >= 16 and edad < 18):
        print("Con permiso de los padres")
    elif (edad >= 18 and edad < 60):
        print("Licencia normal")
    elif (edad >= 60 and edad < 80):
        print("Renovar cada 5 años")
    elif (edad >= 80 and edad < 100):
        print("Renovar cada año")
    else:
        print("Edad invalida")
    print("--------------------------------\n")
