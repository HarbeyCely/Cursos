# PROGRAMA PARA MOSTRAR NOTAS
print("Bienvenido, estas son sus notas")
nota = float(input("Introduzca sus nota obtenida: "))
if (nota>0 and nota<=60):
    print("Esta PFU")
else:
    if (nota>60 and nota<=70):
        print("Paso raspando")
    else:
        if (nota>70 and nota<=85):
            print("Estudiante notable")
        else:
            if (nota>85 and nota<=99):
                print("Estudiante sobresaliente")
            else:
                if (nota==100):
                    print("Matricula de honor")
    