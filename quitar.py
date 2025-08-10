#Funcion de quitar del reporte de ventas una venta

from archivo2 import leer_venta_csv
import pandas as pd 

def remover_venta():
    eliminar_producto=input("Escriba el producto que desea eliminar de la lista de ventas: ")
    df = leer_venta_csv()
    df= df[df['Producto Vendido'] != eliminar_producto]
    print(df)
    print("El producto se ha eliminado con exito")
    #Guardar en inventario
    df.to_csv("ventas.csv", index=False)