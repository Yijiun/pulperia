# Este seria el archivo de ventas

import  pandas as pd

def leer_venta_csv():
    """
        Esta funcion va a leer el venta en formato csv
    """
    try:
        archivo = "ventas.csv"
        df = pd.read_csv(archivo)
    
        return df
    except:
        print("El archivo no existe")