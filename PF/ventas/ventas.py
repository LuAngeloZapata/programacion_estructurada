from conexionventas import *

def registrar_venta(venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario):
    try:
        subtotal = cantidad * precio_unitario
        sql = """INSERT INTO ventas 
                 (venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario, subtotal)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario, subtotal)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar venta: {e}")
        return False

def obtener_historial(usuario_id):
    try:
        sql = """SELECT v.venta_id_grupo, p.nombre, v.cantidad, v.subtotal, v.fecha
                 FROM ventas v
                 JOIN productos p ON v.producto_id = p.id
                 WHERE v.usuario_id = %s
                 ORDER BY v.fecha DESC"""
        cursor.execute(sql, (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return []

def obtener_venta_por_grupo(venta_id_grupo):
    try:
        sql = """SELECT p.nombre, v.cantidad, v.precio_unitario, v.subtotal
                 FROM ventas v
                 JOIN productos p ON v.producto_id = p.id
                 WHERE v.venta_id_grupo = %s"""
        val = (venta_id_grupo,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener venta: {e}")
        return []
    
def obtener_ventas_del_dia(fecha):
    try:
        sql = """SELECT venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario, subtotal, fecha
                 FROM ventas
                 WHERE DATE(fecha) = %s"""
        val = (fecha,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener ventas del día: {e}")
        return []

def obtener_historial_completo():
    try:
        sql = """SELECT venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario, subtotal, fecha
                 FROM ventas
                 ORDER BY fecha DESC"""
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener historial completo: {e}")
        return []