from archivo import leer_inventario_csv
from login import iniciar_sesion
from menu import desplegar_menu
from producto import agregar_articulo
from remover  import remover_producto
from actualizar import desplegar_menu_actualizar
from buscar import localizar
from archivo2 import leer_venta_csv
from notificacion import notificacion
from agregar import agregar_venta
from quitar import remover_venta
from salir import salir



        
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
        if opcion == "6":
            print(leer_venta_csv()) 
        if opcion == "7":
            agregar_venta()
        if opcion == "8":
            localizar()
        if opcion == "9":
            remover_venta()
        if opcion == "10":
            salir()   
        

    else:
        print("El usuario y contrasena es incorrecto. Intentelo de nuevo.")
        
        
    
        
