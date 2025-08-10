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
        desplegar_menu() #mostar el menu principal
        opcion = input("Digite la opcion: ")
        if opcion == "1": 
            print(leer_inventario_csv()) # ver el inventario actual
        if opcion == "2":
            agregar_articulo() #Agregar nuevo producto al inventario
        if opcion == "3":
            remover_producto() # remover un producto del inventario
        if opcion == "4":
            desplegar_menu_actualizar() # mostar el menu para actualizar informacion de inventario
        if opcion == "5":
            notificacion() # mostar una notificacion de algun producto que tengas cantidad menos que 5
        if opcion == "6":
            print(leer_venta_csv()) # mostrar el reporte de ventas
        if opcion == "7":
            agregar_venta() #agregar ventas al reporte
        if opcion == "8":
            localizar() # buscar producto por codigo o nombre
        if opcion == "9":
            remover_venta() # remover una venta agregado por error
        if opcion == "10":
            salir()   # salir de menu principal 
        

    else:
        print("El usuario y contrasena es incorrecto. Intentelo de nuevo.")
        
        
    
        
