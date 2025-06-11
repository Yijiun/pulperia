# Este modulo tiene el inventario del productos de la pulperia

#inventario= {"sandia": 10, "manzana": 10, "mango": 10,"banano": 10, "pera": 10, "agua": 20, "gaseosa": 15, "yogurt": 10, "leche": 20,"arroz": 20, "frijoles": 10, "harina": 10,"pan": 10 ,"papel higenico": 30, "toallas": 20, "tomate": 10, "chayote": 10, "papa": 20 }

import  pandas as pd

archivo = 'inventario_productos.csv'
df = pd.read_csv(archivo)
print(df)



