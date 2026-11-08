arreglo = [
    [10, 20, 30, 40, 50],
    [" ana ","maria","Luz","CLAUDIA","peTra olivares", "anDRes ferNAndo"]
]
print(arreglo[1][5].title()) # primera letra mayus (todas las palabras) y las otras minus
print(arreglo[1][4].capitalize()) # primera letra mayus (solo la primera palabra) y las otras minus
print(arreglo[1][3].lower()) # todo minus
print(arreglo[1][2].swapcase()) # intercambia mayus y minus
print(arreglo[1][1].upper()) # todo mayus
print(arreglo[1][0].strip()) # elimina espacios en blanco