#Funcion del agregar el producto nuevo
from archivo import leer_inventario_csv
import pandas as pd

def agregar_articulo():
    nuevo_producto = input("Digite el nombre del nuevo producto para agregar al inventario: ")
    cantidad_producto = input("Digite la cantiad del producto: ")
    agregar_categoria=  input("Digite la categoria del producto: ")
    precio_compra = float(input("Digite el precio de compra: "))
    precio_venta = (precio_compra * 0.4) + precio_compra
    #Guardar en producto nuevo en inventario
    df = leer_inventario_csv()
    #value = df.loc[row_index, 'column_name']
    last_id = df.iloc[-1]['Codigo']
    new_row= pd.DataFrame({'Producto': [nuevo_producto], 'Cantidad': [cantidad_producto], 'Cateogria': [agregar_categoria],'Codigo': [last_id + 1], 'Precio compra': [precio_compra], 'Precio venta':[precio_venta] })
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("inventario_de_productos.csv", index=False)
    print("Se guardo con exito")
    