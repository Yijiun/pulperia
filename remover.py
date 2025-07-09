#Funcion de remover producto

from archivo import leer_inventario_csv
import pandas as pd 

def remover_producto():
    eliminar_producto=input("Escriba el nombre del producto que desea eliminar de la lista: ")
    df = leer_inventario_csv()
    df= df[df['Producto'] != eliminar_producto]
    print(df)
    print("El producto se ha eliminado con exito")
    #Guardar en inventario
    df.to_csv("inventario_de_productos.csv", index=False)


