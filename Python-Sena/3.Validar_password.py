# VERIFICAR PRIMERO EL USUARIO Y DESPUES LA CONTRASEÑA
usuario_correcto = "admin"
password_correcto = "1234"
usuario_ingresado = input("Ingrese el usuario: ")
if (usuario_ingresado == usuario_correcto):
    password_ingresada = input("Ingrese la contraseña: ")
    if (password_ingresada == password_correcto):
        print("Ha ingresado exitosamente")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")