#Actualizar la producto y los detalles

from archivo import leer_inventario_csv
import pandas as pd

#Seleccionar la informacion  que el usuario quiere actualizar

def desplegar_menu_actualizar(): 
    print("Estos son las siguientes opciones que puede actualizar: ")
    print("1. Actualizar nombre del producto")
    print("2. Actualizar la cantidad de inventario por venta diaria")
    print("3. Actualizar la cantidad de inventario por compra diaria")
    print("4. Actualizar la categoria del producto")
    print("5. Actualizar el precio de compra del producto")

    opcion = input("Digite la opcion requerida: ")
    df = leer_inventario_csv()
    editar(df, opcion)

    
def editar(df, opcion):
    try:
        codigo_producto= int(input("Digite el codigo del producto: "))
        if opcion == "1":
            nuevo_nombre_producto = input("Digite el nuevo nombre del producto: ")
            df.loc[df['Codigo'] == codigo_producto, ['Producto']] = \
                [nuevo_nombre_producto]
            print("El nuevo nombre del producto ha sido aplicado con exito")
        if opcion == "2":
            cantidad_resta = int(input("Digite la cantidad vendida del producto: ")) 
            df.loc[df['Codigo'] == codigo_producto, ['Cantidad']] -= cantidad_resta
            print("La cantidad vendida a sido actualizado en el inventario")
        if opcion == "3":
            cantidad_suma= int(input("Digite la cantidad que quiera agregar al producto: "))
            df.loc[df['Codigo'] == codigo_producto, ['Cantidad']] += cantidad_suma
            print("La cantidad digitada ha sido actualizada en el inventario")
        if opcion == "4":
            nueva_categoria= input("Cual seria la nueva categoria del producto: ")
            df.loc[df['Codigo'] == codigo_producto, ['Categoria']] = \
                [nueva_categoria]
            print("La nueva categoria digitada se ha modificado con exito.")
        if opcion == "5":
            nuevo_precio_compra= float(input("Cual seria el nuevo precio de compra del producto: "))
            nuevo_precio_venta = (nuevo_precio_compra * 0.4) + nuevo_precio_compra
            df.loc[df['Codigo'] == codigo_producto, ['Precio compra', 'Precio venta']] = \
                [nuevo_precio_compra, nuevo_precio_venta]
            print("El nuevo precio de compra y ven han sido actualizados.")    
    #Guardar datos del inventario
        df.to_csv("inventario_de_productos.csv", index=False)
        print(df)
    except ValueError:
        print("Error: El valor debe ser una serie de numeros, por favor ingrese el codigo.")
    


    
    
    