
import mysql.connector
from mysql.connector import Error
import os

alumno = {}
contraseña = "angelo1"

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"⚠️ Error de conexión: {e}")
        return None

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\nPresiona cualquier tecla para continuar...")

def agregarCalificaciones():
    borrarPantalla()
    print("\n\t.:: ➕ Agregar Calificaciones ::.\n")

    alumno["nombre"] = input("👤 Nombre del alumno: ").upper().strip()
    alumno["cal1"] = float(input("📌 Calificación 1: "))
    alumno["cal2"] = float(input("📌 Calificación 2: "))
    alumno["cal3"] = float(input("📌 Calificación 3: "))

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    sql = "INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)"
    valores = (alumno["nombre"], alumno["cal1"], alumno["cal2"], alumno["cal3"])

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        print("\n✅ Registro exitoso.")
    except Exception as e:
        print(f"\n❌ Error al insertar: {e}")
    finally:
        cursor.close()
        conexion.close()
    esperarTecla()

def mostrarCalificaciones():
    borrarPantalla()
    print("\n\t.:: 📋 Mostrar Calificaciones ::.\n")

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos")
    registros = cursor.fetchall()

    if registros:
        print(f"{'ID':<5}{'Nombre':<20}{'Cal1':<10}{'Cal2':<10}{'Cal3':<10}")
        print("-"*50)
        for reg in registros:
            print(f"{reg[0]:<5}{reg[1]:<20}{reg[2]:<10}{reg[3]:<10}{reg[4]:<10}")
    else:
        print("⚠️ No hay registros.")

    cursor.close()
    conexion.close()
    esperarTecla()

def buscarAlumno():
    borrarPantalla()
    print("\n\t.:: 🔍 Buscar Alumno ::.\n")
    nombre = input("Nombre del alumno: ").upper().strip()

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE nombre = %s", (nombre,))
    alumno = cursor.fetchone()

    if alumno:
        print(f"\n👤 Nombre: {alumno[1]}")
        print(f"📌 Calificaciones: {alumno[2]}, {alumno[3]}, {alumno[4]}")
        promedio = (alumno[2] + alumno[3] + alumno[4]) / 3
        print(f"🎯 Promedio: {promedio:.2f}")
    else:
        print("🚫 Alumno no encontrado.")

    cursor.close()
    conexion.close()
    esperarTecla()

def borrarAlumno():
    borrarPantalla()
    print("\n\t.:: 🗑️ Borrar Alumno ::.\n")
    nombre = input("Nombre del alumno a borrar: ").upper().strip()

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    cursor.execute("DELETE FROM alumnos WHERE nombre = %s", (nombre,))
    conexion.commit()

    if cursor.rowcount > 0:
        print("✅ Alumno eliminado.")
    else:
        print("🚫 Alumno no encontrado.")

    cursor.close()
    conexion.close()
    esperarTecla()

def modificarAlumno():
    borrarPantalla()
    print("\n\t.:: ✏️ Modificar Alumno ::.\n")
    nombre = input("Nombre del alumno a modificar: ").upper().strip()

    conexion = conectar()
    if conexion is None:
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE nombre = %s", (nombre,))
    alumno = cursor.fetchone()

    if alumno:
        nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ").upper().strip() or alumno[1]
        nueva1 = input("Nueva calificación 1 (Enter para no cambiar): ")
        nueva2 = input("Nueva calificación 2 (Enter para no cambiar): ")
        nueva3 = input("Nueva calificación 3 (Enter para no cambiar): ")

        cal1 = float(nueva1) if nueva1 else alumno[2]
        cal2 = float(nueva2) if nueva2 else alumno[3]
        cal3 = float(nueva3) if nueva3 else alumno[4]

        sql = "UPDATE alumnos SET nombre = %s, cal1 = %s, cal2 = %s, cal3 = %s WHERE id = %s"
        val = (nuevo_nombre, cal1, cal2, cal3, alumno[0])
        cursor.execute(sql, val)
        conexion.commit()
        print("✅ Alumno modificado.")
    else:
        print("🚫 Alumno no encontrado.")

    cursor.close()
    conexion.close()
    esperarTecla()
