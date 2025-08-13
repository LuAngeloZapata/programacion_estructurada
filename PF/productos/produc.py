from conexionventas import *

def agregar_producto(nombre, precio, cantidad=0):
    try:
        sql = """INSERT INTO productos (nombre, precio, cantidad) 
                 VALUES (%s, %s, %s)
                 ON DUPLICATE KEY UPDATE 
                 cantidad = cantidad + VALUES(cantidad),
                 precio = VALUES(precio)"""
        val = (nombre, precio, cantidad)
        cursor.execute(sql, val)
        conexion.commit()
        return cursor.lastrowid or True
    except Exception as e:
        print(f"Error al agregar producto: {e}")
        return False

def obtener_productos():
    try:
        cursor.execute("SELECT id, nombre, precio, cantidad FROM productos")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []

def buscar_producto(nombre):
    try:
        sql = "SELECT id, nombre, precio, cantidad FROM productos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        return cursor.fetchone()
    except Exception as e:
        print(f"Error al buscar producto: {e}")
        return None

def actualizar_stock(id_producto, cantidad):
    try:
        sql = "UPDATE productos SET cantidad = cantidad + %s WHERE id = %s"
        val = (cantidad, id_producto)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar stock: {e}")
        return False
def eliminar_producto(producto_id):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM ventas WHERE producto_id = %s", (producto_id,))
            cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
            conexion.commit()
            return True
    except mysql.connector.Error as error:
        print(f"\n❌ Error al eliminar producto: {error}")
        conexion.rollback()
        return False
    
def buscar_producto_por_id(producto_id):
    try:
        sql = "SELECT id, nombre, precio, cantidad FROM productos WHERE id = %s"
        val = (producto_id,)
        cursor.execute(sql, val)
        return cursor.fetchone()  
    except Exception as e:
        print(f"Error al buscar producto por ID: {e}")
        return None
import os
from datetime import datetime
import pandas as pd 
    
def exportar_inventario():
        """Prepara los datos del inventario para exportación"""
        productos = obtener_productos()
        if not productos:
            return None, None
            
        
        datos = []
        for p in productos:
            datos.append({
                'id': p[0],
                'nombre': p[1],
                'precio': f"${p[2]:.2f}",
                'cantidad': p[3]
            })
        
        columnas = ['id', 'nombre', 'precio', 'cantidad']
        return datos, columnas
    
def generar_excel( datos, columnas):
        """Genera archivo Excel con el inventario"""
        try:
            
            os.makedirs('reportes', exist_ok=True)
            
            
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reportes/inventario_{fecha}.xlsx"
            
            
            df = pd.DataFrame(datos, columns=columnas)
            df.to_excel(nombre_archivo, index=False)
            
            return nombre_archivo
        except Exception as e:
            print(f"Error al generar Excel: {str(e)}")
            return None