from conexionventas import conexion, cursor
import datetime
import hashlib

# Función para hashear la contraseña
def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Registro de usuario
def registrar(nombre, apellidos, email, contrasena):
    try:
        fecha = datetime.datetime.now()
        contrasena = hash_password(contrasena)
        sql = "INSERT INTO usuarios (usuario, apellidos, email, password, fecha) VALUES (%s,%s, %s,%s,%s)"
        val = (nombre, apellidos, email, contrasena, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

# Inicio de sesión
def iniciar_sesion(usuario, contrasena):
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT id, usuario FROM usuarios WHERE usuario = %s AND password = %s"
        val = (usuario, contrasena)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            return registro  # (id, usuario)
        else:
            return None
    except:
        return None
