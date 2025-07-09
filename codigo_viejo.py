#Pedir al usuario el nombre del producto y la cantidad para restar

from archivo import df

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