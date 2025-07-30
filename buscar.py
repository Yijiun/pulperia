#Buscar producto por  nombre o  codigo  y ver los detalles


from archivo import leer_inventario_csv
import pandas as pd


def localizar():
    # Cargar CSV
    df = leer_inventario_csv()

    # Definir el valor que necesito buscar 
    target_name = input("Digite el nombre del producto")
    target_code = float(input("Digite el producto por codigo"))

    # Filter rows where both name and code match
    filtered_rows = df[(df['Producto'] == target_name) & (df['Codigo'] == target_code)]

    # Show the result
    print(filtered_rows)