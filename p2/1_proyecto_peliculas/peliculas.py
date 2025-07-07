import os
CONTRASEÑA="angelo"
peliculas = []

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona Enter para continuar...")

def agregarPeliculas():
    resp = "si"
    while resp == "si":
        nombre = input("\🍿Ingresa el nombre de la película: ").strip().upper()
        if nombre == "":
            print("✖️ El nombre no puede estar vacío.")
        elif nombre in peliculas:
            print("⚠️ Esa película ya fue agregada.")
        else:
            peliculas.append(nombre)
            print(f" '{nombre}' fue agregada.")
        resp = input("¿Deseas agregar otra película? (si/no): ").lower()

def eliminarPeliculas():
    clave=input("U0001F464Ingresa una contraseña: ")
    if clave !=CONTRASEÑA:
        print("!Contraseña invalida!")
        return
    nombre = input("🍿Ingresa el nombre de la película a eliminar: ").strip()
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"'{nombre}' fue eliminada.")
    else:
        print("⚠️ La película no se encontró.")

def modificarPeliculas():
    consultarPeliculas()
    nombre = input("🍿Ingresa el nombre de la película que quieres modificar: ").strip()
    if nombre in peliculas:
        nuevo = input("Ingresa el nuevo nombre: ").strip()
        index = peliculas.index(nombre)
        peliculas[index] = nuevo
        print(f" '{nombre}' fue modificada a '{nuevo}'.")
    else:
        print("✖️ La película no se encontró.")

def consultarPeliculas():
    print("\n Lista de películas:")
    if peliculas:
        for i, peli in enumerate(peliculas, start=1):
            print(f"{i}. {peli}")
    else:
        print("No hay películas registradas.")

def buscarPeliculas():
    nombre = input("🍿Ingresa el nombre de la película a buscar: ").strip()
    if nombre in peliculas:
        print(f" '{nombre}' sí está registrada.")
    else:
        print(" La película no se encontró.")

def vaciarPeliculas():
    clave=input("Ingresa una contraseña: ")
    if clave !=CONTRASEÑA:
        print("!Contraseña invalida!")
        return
    peliculas.clear()
    print("⚠️ Lista vacía. Todas las películas fueron eliminadas.")
    resp=input("Deseas quitar todas las peliculas del sistema? (si/no)").lower().strip()
