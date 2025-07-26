from conexionBD import *

def crear(usuario_id,titulo,descripcion):
    try:
        cursor.execute("INSERT INTO notas(usuario_id,titulo,descripcion,fecha) Values (%s,%s,%s,NOW())",(usuario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("SELECT * FROM notas WHERE usuario_id=%s", (usuario_id,))
        listas=cursor.fetchall()
        return listas
    except:
        return []
    
def cambiar(id,titulo,descripcion):
    try:
        cursor.execute("UPDATE notas SET titulo=%s,descripcion=%s,fecha=Now() WHERE id=%s",(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False
    
def borrar(id):
    try:
        cursor.execute("DELATE FROM notas WHERE id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False