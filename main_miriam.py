#crear un usuario sin que se muestre contrasena 
# import getpass

# usuarios = {}

# for i in range(1, 5):
#     print(f"\nCreando el usuario #{i}")
#     nombre = input("Ingresa el nombre de usuario: ")
#     while nombre in usuarios:
#         print("Ese nombre de usuario ya existe. Intenta con otro.")
#         nombre = input("Ingresa el nombre de usuario: ")
    
#     contrasena = getpass.getpass("Ingresa la contraseña (no se mostrará): ")
#     usuarios[nombre] = contrasena

# print("\nUsuarios creados:")
# for usuario in usuarios:
#     print(f"- {usuario}")

#introduccion del producto 
# try:
#     producto = input("Introducir el nombre del producto: ")
#     cantidad = int(input("Introduzca la cantidad vendida del producto: "))
#crear nuevo producto 
inventario = {}

# Función para añadir un nuevo producto
def agregar_producto():
    nombre = input("Nombre del producto: ")
    
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
    else:
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"Producto '{nombre}' añadido con éxito.")
        except ValueError:
            print("Error: Ingrese un número válido para el precio o la cantidad.")
        finally:
            print("Intente nuevamente")  

# Ejemplo de uso
agregar_producto()

from archivo import df


#Pedir al usuario el nombre del producto y la cantidad para restar
try:
    producto = input("Introducir el nombre del producto: ")
    cantidad = int(input("Introduzca la cantidad vendida del producto: "))


#Revisar si el producto existe dentro del inventario
    if producto in df["Producto"].values:
        df.loc[df["Producto"] == producto, "Cantidad"] -= cantidad
        #Evitar que el usuario agregue un numero negativo
        df["Cantidad"] = df["Cantidad"].apply(lambda x: max(x,0))
        print("/nInventario actual:")
        print(df)
        
        #Guardar cambios en el mismo csv
        df.to_csv("inventario_productos.csv", index=False)
    else:
        print("Este producto no existe en el inventario")
    
except ValueError:
    print("Error: Ingrese un numero valido para la cantidad")
except Exception as e:
    print(f'Se ha producido un error inesperado: {e}')
        
