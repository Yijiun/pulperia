#Usuarios para log in a la aplicacion de pulperia

def iniciar_sesion():
    while True:
        try:
            usuario_digitado =str(input("Digite su usuario: "))
            password = input("Ingrese  su contrasena: ")
            if usuario_digitado == "Yi" and password == "1234":
                return True #El valor ocupa retornar
                print("Hola Yi")
            if usuario_digitado == "Oscar" and password == "1234":
                return True
                print("Hola Oscar")
            if usuario_digitado == "Patricia" and password == "1234":
                return True
                print("Hola Patricia")
            if usuario_digitado == "Kevin" and password == "1234":
                return True
                print("Hola Kevin")
            break     
        except ValueError:
            print("Error el usuario no existe")
        finally:
            print("Por favor selecciona la opcion de servicio")  
            
    