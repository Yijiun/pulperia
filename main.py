from archivo import leer_inventario_csv
from menu import desplegar_menu
from producto import agregar_articulo
from remover  import remover_producto
from actualizar import desplegar_menu_actualizar


        
if __name__ == "__main__":
    nombre_usuario= "E" 
    contrasena =  "1234" 
    
    usuario_digitado = input("Digite su usuario: ")
    contrasena_digitada = input("Digite su contrasena: ")
    
    if usuario_digitado == nombre_usuario and contrasena_digitada == contrasena:
        print("Hola, Eduardo")
        desplegar_menu()
        opcion = input("Digite la opcion: ")
        if opcion == "1": 
            print(leer_inventario_csv())
        if opcion == "2":
            agregar_articulo()
        if opcion == "3":
            remover_producto()
        if opcion == "4":
            desplegar_menu_actualizar()
        

    else:
        print("El usuario y contrasena es incorrecto. Intentelo de nuevo.")
        
        
    
        
