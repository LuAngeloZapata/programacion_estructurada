import mysql.connector
from mysql.connector import Error
peliculas=[]
contraseña = "angelo1"  

#dict u objetos para los atributos (Nombre, Categoria, clasificacion, genero, idioma)

#peliculas={
#            "nombre":"",
#            "Categorias":"",
#            "clasificasion":"",
#            "genero":"",
#           "idiomas":""
#           }

pelicula={}
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima culaquier tecla para continuar ...")   

def CrearPeliculas():
    borrarPantalla()
    print("\n\t.::📽️  Alta de películas ::.\n")

    pelicula["nombre"] = input("🔎Ingresa el nombre: ").upper().strip()
    pelicula["categoria"] = input("🍿Ingresa la Categoría: ").upper().strip()
    pelicula["clasificacion"] = input("🅰️Ingresa la Clasificación: ").upper().strip()
    pelicula["genero"] = input("Ingresa el Género: ").upper().strip()
    pelicula["idioma"] = input("㊙️Ingresa el Idioma: ").upper().strip()

    conexion = conectar()
    if conexion is None:
        print("⚠️No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()
    try:
        sql = "INSERT INTO peliculas (id, nombre, categoria, clasificacion, genero, idioma) VALUES (NULL, %s, %s, %s, %s, %s)"
        valores = (
            pelicula["nombre"],
            pelicula["categoria"],
            pelicula["clasificacion"],
            pelicula["genero"],
            pelicula["idioma"]
        )
        cursor.execute(sql, valores)
        conexion.commit()
        print("\n\t\t ::: ✅¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    except Exception as e:
        print(f"\n\t❌ Error al insertar en la base de datos: {e}")
    finally:
        cursor.close()
        conexion.close()

    esperarTecla()





def conectar():
   try:
         conexion=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="",
         database="bd_peliculas"
      )
         return conexion
   except Error as e:
      print(f"⚠️El error que sucedio es: {e}")
      return None

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.::🔎 Consultar o Mostrar las películas ::.\n")

    conexion = conectar()
    if conexion is None:
        print("⚠️No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM peliculas")
        resultados = cursor.fetchall()

        if len(resultados) == 0:
            print("\t.:: ❌No hay películas registradas en la base de datos ::.")
        else:
            for peli in resultados:
                print("🍿Mostrar las peliculas")
                print(f"")
                print(f"\n📽️  ID: {peli[0]}")
                print(f"   Nombre: {peli[1]}")
                print(f"   Categoría: {peli[2]}")
                print(f"   Clasificación: {peli[3]}")
                print(f"   Género: {peli[4]}")
                print(f"   Idioma: {peli[5]}")

    except Exception as e:
        print(f"\n❌ Error al consultar: {e}")
    finally:
        cursor.close()
        conexion.close()

    esperarTecla()

def buscarPeliculas():
  borrarPantalla()
  conexion=conectar()
  if conexion!=None:
    print("\n\t.::🔎 Buscar Películas ::. \n")
    nombre=input("🍿Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexion.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: ❌peliculas no encontradas en el sistema ::..")
def borrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Borrar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def modificarPeliculas():
  borrarPantalla()
  conexion = conectar()
  if conexion != None:
    print("\n\t.::♻️ Modificar Películas ::. \n")
    pelicula["nombre"] = input("🍿Ingresa el nombre de la película a modificar: ").upper().strip()
    cursor = conexion.cursor()
    sql = "select * from peliculas where nombre=%s"
    val = (pelicula["nombre"],)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    if registros:
      print("Ingresa los nuevos datos (deja vacío para no cambiar):")
      pelicula.update({"nombre": input("Nuevo nombre: ").upper().strip() or registros[0][1]})
      pelicula.update({"categoria": input("Nueva categoría: ").upper().strip() or registros[0][2]})
      pelicula.update({"clasificacion": input("Nueva clasificación: ").upper().strip() or registros[0][3]})
      pelicula.update({"genero": input("Nuevo género: ").upper().strip() or registros[0][4]})
      pelicula.update({"idioma": input("Nuevo idioma: ").upper().strip() or registros[0][5]})

      sql_update = "update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
      val_update = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], registros[0][1])
      cursor.execute(sql_update, val_update)
      conexion.commit()
      print("\n\t\t::: ✅¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
      print("\t .:: ❌Película no encontrada en el sistema ::..")      

#def agregarCaracteristucapeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Caracteristica a peliculas ::.\n ")
    atributo=input("Ingresar la nueva caracteristica de la pelicula: ").lower().strip()
    valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    #pelicula.update({atributo:valor})
    pelicula[atributo]=valor
    print("\n\t\t ::: ¡LA OPERACION SE REALISO CON EXITO! :::")

#def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Características de una Película  ::.\n")

    nombre = input("Ingresa el nombre de la película que deseas modificar: ").strip().upper()

    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre,))
        peli = cursor.fetchone()

        if peli:
            print("\n\tValores actuales:")
            for campo, valor in peli.items():
                print(f"  {campo} : {valor}")

            campo_a_modificar = input("\n¿Qué característica deseas modificar? (Ej. categoria, clasificacion, genero, idioma): ").lower().strip()

            if campo_a_modificar not in peli:
                print("\n\t⚠️ La característica no existe.")
            else:
                nuevo_valor = input(f"Ingrese el nuevo valor para {campo_a_modificar}: ").strip().upper()
                sql = f"UPDATE peliculas SET {campo_a_modificar} = %s WHERE nombre = %s"
                cursor.execute(sql, (nuevo_valor, nombre))
                conexion.commit()
                print("\n\t✅ ¡La característica fue modificada exitosamente!")
        else:
            print("\n\t🚫 No se encontró ninguna película con ese nombre.")
    except Exception as e:
        print(f"\n❌ Error al modificar: {e}")
    finally:
        cursor.close()
        conexion.close()

    esperarTecla()

#def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de una Película ::.\n")

    nombre = input("Ingresa el nombre de la película: ").strip().upper()
    intento = input("Ingresa la contraseña para continuar: ").strip()

    if intento != contraseña:
        print("\n\t🔒 Contraseña incorrecta. No se puede continuar.")
        esperarTecla()
        return

    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM peliculas WHERE nombre = %s", (nombre,))
        peli = cursor.fetchone()

        if peli:
            print("\n\tCaracterísticas actuales:")
            for campo, valor in peli.items():
                print(f"  {campo}: {valor}")

            campo_a_borrar = input("\n¿Qué característica deseas eliminar (vaciar)? ").lower().strip()

            if campo_a_borrar not in peli:
                print("\n\t⚠️ Esa característica no existe.")
            else:
                sql = f"UPDATE peliculas SET {campo_a_borrar} = NULL WHERE nombre = %s"
                cursor.execute(sql, (nombre,))
                conexion.commit()
                print("\n\t✅ ¡La característica fue borrada exitosamente!")
        else:
            print("\n\t🚫 No se encontró ninguna película con ese nombre.")
    except Exception as e:
        print(f"\n❌ Error al borrar: {e}")
    finally:
        cursor.close()
        conexion.close()

    esperarTecla()
