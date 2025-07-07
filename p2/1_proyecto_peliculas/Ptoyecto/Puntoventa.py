

usuarios = []
contraseñas = []
inventario = []         
historial_ventas = []
def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("Oprima culaquier tecla para continuar ...")  

def Usuario_password():
     print("\n\t\t\t:: '\U0001F64C' Bienvenido al punto de venta Mini Super OLZA  ::")
    
     while True:
        usuario_ingresado = input("\U0001F464Ingresa tu usuario: ").strip()

        if usuario_ingresado in usuarios:
            indice = usuarios.index(usuario_ingresado)
            contraseña_ingresada = input("\U0001F510Ingresa tu contraseña: ").strip()

            if contraseña_ingresada == contraseñas[indice]:
                print(f"\n\U0001F64CBienvenido nuevamente, {usuario_ingresado}!")
                return usuario_ingresado  # ← devolvemos el nombre
            else:
                print("\n\u274CContraseña incorrecta.\n")
                return None
        else:
            print("\n\u274CUsuario no encontrado.\u274C")
            resp = input("\U0001F464¿Deseas crear un nuevo usuario? (Si/No): ").strip().lower()
            
            if resp == "si":
                nuevo_usuario = input("\U0001F464Ingresa un nuevo nombre de usuario: ").strip()
                
                if nuevo_usuario in usuarios:
                    print("\u26A0Ese usuario ya existe. Intenta con otro.\u26A0\n")
                else:
                    nueva_contraseña = input("\U0001F510Crea tu contraseña: ").strip()
                    usuarios.append(nuevo_usuario)
                    contraseñas.append(nueva_contraseña)
                    print(f"\n\u2705Usuario '{nuevo_usuario}' creado con éxito.\u2705\n")
            else:
                print("\n\u274CNo se ha creado ningún usuario.\u274C\n")
                return None

def Menu_Principal(nombre_usuario):
    print(f"\U0001F64CBien benido {nombre_usuario}")
    print("\n\t\t\t :::\U0001F6D2Mini Super OLZA\U0001F6D2:::: \n 1.- Agrgar Nuevo Producto  \n 2.- Inventario  \n 3.- Vender  \n 4.- Historial de venta  \n 5.-Borrar producto  \n 6.- Inicio \n 7.-Salir")
    opcion=input("\t Eliga una opcion: ").strip()
    return opcion

def AgregarProducto(inventario):
    print("\n" + "="*40)
    print("\t--- \U0001F4E6Agregar Nuevo Producto\U0001F4E6 ---")
    print("="*40)
    nombre = input("\U0001F4E6Nombre del producto: ").strip().capitalize()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("❌ Error: precio o cantidad no válidos.")
        return

    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] += cantidad
            print(f"✔ Producto existente. Se sumaron {cantidad} unidades a '{nombre}'.")
            return

    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(nuevo)
    print(f"✔ Producto '{nombre}' agregado con éxito.")

def Inventario(inventario):
    print("\n\t\t--- \U0001F4E6Inventario Actual ---")
    if not inventario:
        print("\u26A0El inventario está vacío.\u26A0")
        return

    for idx, producto in enumerate(inventario, start=1):
        print(f"{idx}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

def VenderProducto(inventario, historial_ventas):
    print("\n\t\t--- \U0001F6D2Venta de Producto\U0001F6D2 ---")
    nombre = input("\U0001F6D2Nombre del producto: ").strip().capitalize()
    
    # Buscar producto en el inventario
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"🧾Disponible: {producto['cantidad']} unidades")
            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("❌ Error: cantidad no válida.")
                return

            if cantidad > producto["cantidad"]:
                print("❌ No hay suficiente stock.")
                return

            producto["cantidad"] -= cantidad
            total = producto["precio"] * cantidad

            venta = {"producto": nombre, "cantidad": cantidad, "total": total}
            historial_ventas.append(venta)

            print(f"✔ Venta realizada: {cantidad} x {nombre} = ${total:.2f}")
            return

    print("❌ Producto no encontrado en inventario.")

def HistorialVenta(historial_ventas):
    print("\n\t\t---\U0001F4BE Historial de Ventas\U0001F4BE ---")
    if not historial_ventas:
        print(" ❌ No hay ventas registradas.")
        return

    total_general = 0
    for idx, venta in enumerate(historial_ventas, start=1):
        print(f"{idx}. {venta['producto']} - Cantidad: {venta['cantidad']} - Total: ${venta['total']:.2f}")
        total_general += venta["total"]

    print(f"\n🧾 Total acumulado de ventas: ${total_general:.2f}")

def BorrarProducto(inventario):
    print("\n" + "="*40)
    print("\t\t \U0001F5D1BORRAR PRODUCTO")
    print("="*40)

    nombre = input("Nombre del producto a borrar: ").strip().capitalize()

    for i, producto in enumerate(inventario):
        if producto["nombre"] == nombre:
            print("\n" + "-"*40)
            print(f" ✅Producto encontrado: {nombre}")
            print(f"Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            print("-"*40)
            confirm = input(f"¿Seguro que quieres borrar '{nombre}'? (Si/No): ").strip().lower()
            if confirm == "si":
                inventario.pop(i)
                print(f"\n✅ Producto '{nombre}' borrado exitosamente.")
            else:
                print("\n⚠️ Operación cancelada por el usuario.")
            return

    print("\n❌ Producto no encontrado en inventario.")
    print("="*40)
