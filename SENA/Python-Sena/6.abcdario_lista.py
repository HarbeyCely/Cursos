abcedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
print(abcedario)
print("Cantidad de caracteres antes ",len(abcedario))
for i in range(len(abcedario), 1, -1):
    if i % 3 == 0:
        abcedario.pop(i-1)        
print(abcedario)
print("Cantidad de caracteres despues ",len(abcedario))

