from archivo import leer_inventario_csv
import pandas as pd

def notificacion():
    # Cargar el archivo
    df = leer_inventario_csv()
    # Filtrar producto por cantidad < 5
    filtered_df = df[df['Cantidad'] < 5]
    # Mostrar solo el nombre del proudcto y la cantidad
    result = filtered_df[['Producto', 'Cantidad']]
    # Mostrar resultado
    print("Es hora de que comprar estos productos nuevamente")
    print(result)