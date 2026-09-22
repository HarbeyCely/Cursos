# GUSTOS DE COMIDAS
comida = input("Mi comida preferida es: ").strip().lower()
if (comida.rstrip('s') == "hamburguesa"):
    print("Me gustan las hamburguesas.")
elif (comida == "perro"):
    print("Me gustan los perros.")
elif (comida == "Salchipapa"):
    print("Me gusta la salchipapa.")
elif (comida == "burrito"):
    print("Me gustan los burritos.")
elif (comida == "taco"):
    print("Me gustan los tacos.")
else:
    print("Me gustan otras comidas.")