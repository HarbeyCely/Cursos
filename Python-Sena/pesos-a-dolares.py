# Programa para cambiar el equivalente de pesos a dolares
pesos = float(input("Ingrese la cantidad de pesos colombianos: "))
pesos_por_dolar = 3130.58
equivalencia = pesos / pesos_por_dolar
print(f"La equivalencia de {pesos} pesos colombianos en dolares es: {round(equivalencia,2)} USD")