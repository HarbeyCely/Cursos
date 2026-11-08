# Que reciba el numero de años que tiene nuestro computador, mayor a 2 viejo y menor a 2 nuevo

years = int(input("Ingrese los años que tiene su PC: "))
if (years>=0 and years <= 2):
    print("Su computador es nuevo")
else:
    print("Su computador es viejo")