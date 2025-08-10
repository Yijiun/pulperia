# Crear un csv para agregar las ventas 

import pandas as pd
from archivo2 import leer_venta_csv

def agregar_venta():
    producto_vendido = str(input("Digite el nombre del producto vendido: "))
    cantidad_vendida = int(input("Digite la cantidad vendida el producto"))
    fecha = str(input("Digite la fecha de hoy con este formato Año/Mes/Dia"))
    precio_compra = float(input("Digite el precio de compra: "))
    precio_venta = (precio_compra * 0.4) + precio_compra
    suma_total = float(cantidad_vendida * precio_venta)
    #Guardar la venta
    df = leer_venta_csv()
    #Agregar datos de la venta
    new_row= pd.DataFrame({'Producto Vendido': [producto_vendido], 'Cantidad': [cantidad_vendida], 'Fecha': [fecha],'Precio de compra': [precio_compra], 'Precio de venta': [precio_venta], 'Suma total':[suma_total] })
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("ventas.csv", index=False)
    print("Se guardo con exito")