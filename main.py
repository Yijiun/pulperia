from archivo import leer_inventario_csv
from menu import desplegar_menu
from producto import agregar_articulo


# #Pedir al usuario el nombre del producto y la cantidad para restar
# try:
#     producto = input("Introducir el nombre del producto: ")
#     cantidad = int(input("Introduzca la cantidad vendida del producto: "))


# #Revisar si el producto existe dentro del inventario
#     if producto in df["Producto"].values:
#         df.loc[df["Producto"] == producto, "Cantidad"] -= cantidad
#         #Evitar que el usuario agregue un numero negativo
#         df["Cantidad"] = df["Cantidad"].apply(lambda x: max(x,0))
#         print("/nInventario actual:")
#         print(df)
        
#         #Guardar cambios en el mismo csv
#         df.to_csv("inventario_de_productos.csv", index=False)
#     else:
#         print("Este producto no existe en el inventario")
    
# except ValueError:
#     print("Error: Ingrese un numero valido para la cantidad")
# except Exception as e:
#     print(f'Se ha producido un error inesperado: {e}')
        
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
            
        

    else:
        print("El usuario y contrasena es incorrecto. Intentelo de nuevo.")
        
        
    
        
