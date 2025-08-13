import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")


def esperarTecla():
    input("\nPresiona ENTER para continuar...")


def menu_principal():
    print("\n\t..:: Bienvenido a MiniSuperOLZA 🛒 ::..\n")
    print("1️⃣ - Registrarse")
    print("2️⃣ - Iniciar Sesión")
    print("3️⃣ - Salir")
    return input("\nSelecciona una opción: ").strip()


def menu_sistema():
    print("\n\t..:: Menú Principal del Sistema ::..")
    print("1️⃣ - Agregar producto")
    print("2️⃣ - Ver inventario")
    print("3️⃣ - Realizar venta")
    print("4️⃣ - Historial de ventas")
    print("5️⃣ - Eliminar producto")
    print("6️⃣ - Exportar inventario")
    print("7️⃣ - Cerrar secion")
    return input("\nSelecciona una opción: ").strip()


def mostrar_productos(lista_productos):
    if not lista_productos:
        print("\n❌ No hay productos registrados.")
        return

    print(f"\n{'ID':<5} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
    print("-" * 50)
    for prod in lista_productos:
        print(f"{prod[0]:<5} {prod[1]:<20} ${prod[2]:<10.2f} {prod[3]:<10}")


def mostrar_ventas(lista_ventas):
    if not lista_ventas:
        print("\n❌ No hay ventas registradas.")
        return

    print(f"\n{'ID':<5} {'Producto':<20} {'Cantidad':<10} {'Fecha':<20} {'Vendedor':<15}")
    print("-" * 70)
    for v in lista_ventas:
        print(f"{v[0]:<5} {v[1]:<20} {v[2]:<10} {v[3]:<20} {v[4]:<15}")

