from archivo import leer_inventario_csv
from login import iniciar_sesion
from menu import desplegar_menu
from producto import agregar_articulo
from remover  import remover_producto
from actualizar import desplegar_menu_actualizar
from buscar import localizar
from notificacion import notificacion



        
if __name__ == "__main__":
    
    
    
   # if usuario_digitado == nombre_usuario and contrasena_digitada == contrasena:#
    if iniciar_sesion() == True: 
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
        if opcion == "5":
            notificacion()
        if opcion == "7":
            localizar()
          
            
        

    else:
        print("El usuario y contrasena es incorrecto. Intentelo de nuevo.")
        
        
    
        
