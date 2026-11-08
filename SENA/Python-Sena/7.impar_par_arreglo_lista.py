# IMPARES MAYORES A X
n = int(input("Ingrese mayores a cuanto: "))
A = [1,3,8,5,30,9,13]
B = []
C = []
for i in A:
    if (i>n and i%2!=0):
        B.append(i)
    elif (i>n and i%2==0):
        C.append(i)
print(f"Los numeros impares mayores a {n} son {B}")
print(f"Los numeros pares mayores a {n} son {C}")