#Crear un archivo csv para el reporte de ventas

import pandas as pd


data = {
    "Producto Vendido": ["Sandia", "Detergent", "Arroz"],
    "Cantidad": [40, 20, 10],
    "Fecha": ["2025-08-01", "2025-08-02", "2025-08-03"],
    "Precio de compra": [1200.0, 6935.0, 2653.0],
    "Precio de venta": [1680.0, 9709.0, 2653.0],
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Calcular la "Suma total" (Cantidad * Precio de venta)
df["Suma total"] = df["Cantidad"] * df["Precio de venta"]

# Guardar el DataFrame en un archivo CSV
df.to_csv("ventas.csv", index=False)

# Mostrar el DataFrame
print(df)