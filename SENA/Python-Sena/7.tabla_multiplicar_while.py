# TABLA DE MULTIPLICAR DEL 2 CON TIEMPO Y WHILE
import time
numero = int(input("Ingrese el numero del que desea la tabla: "))
i=1
while i <= 10:
    r = numero * i
    i += 1
    print(f"{numero} X {i-1} = {r}")
    time.sleep(0.8)