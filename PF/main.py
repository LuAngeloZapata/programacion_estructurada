import funciones
from usuarios import usuarios
from productos import produc
from ventas import ventas
import getpass
import random
import pandas as pd
def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_principal()

        if opcion == "1" or opcion.upper() == "REGISTRARSE":
            funciones.borrarPantalla()
            print("\n\t..:: Registro de Usuario ::..")
            nombre = input("\tNombre: ").strip()
            apellido = input("\tApellido del usuario: ").strip()
            email = input("\tCorreo electrónico: ").lower().strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            registrado = usuarios.registrar(nombre, apellido, email, password)
            if registrado:
                print(f"\n✅ Usuario '{nombre} {apellido}' registrado correctamente, con el correo {email}.")
            else:
                print("\n❌ No se pudo registrar el usuario. Intenta con otro nombre.")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "INICIAR SESION":
            funciones.borrarPantalla()
            print("\n\t..:: Iniciar Sesión ::..")
            usuario = input("\tUsuario: ").strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            user_data = usuarios.iniciar_sesion(usuario, password)

            if user_data:
                print(f"\n✅ Bienvenido, {user_data[1]}!")
                menu_usuario(user_data[0], user_data[1])
            else:
                print("\n❌ Usuario o contraseña incorrectos.")
            funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "SALIR":
            print("\n👋 ¡Gracias por usar el sistema de ventas!")
            opcion = False
            funciones.esperarTecla()
        else:
            print("\n⚠️ Opción no válida.")
            funciones.esperarTecla()

def menu_usuario(usuario_id, nombre):
    while True:
        funciones.borrarPantalla()
        print(f"\n..:: Menú del Usuario: {nombre} ::..")
        opcion = funciones.menu_sistema()

        if opcion == "1" or opcion.upper() == "AGREGAR PRODUCTO":
            while True:
              funciones.borrarPantalla()
              print("\n\t..:: Agregar Producto ::..")
              nombre_prod = input("\tNombre del producto: ")
              precio = float(input("\tPrecio: "))
              stock = int(input("\tCantidad: "))
              resultado = produc.agregar_producto(nombre_prod, precio, stock)
              if resultado:
                print(f"\n✅ Producto '{nombre_prod}' agregado correctamente.")
              else:
                print("\n❌ No se pudo agregar el producto.")
              otra = input("\n¿Deseas agregar otro producto? (s/n): ").lower()
              if otra != "s":
               break
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "VER INVENTARIO":
            funciones.borrarPantalla()
            productos = produc.obtener_productos()
            if productos:
                print(f"\n{'ID':<5} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
                print("-" * 50)
                for p in productos:
                    print(f"{p[0]:<5} {p[1]:<20} ${p[2]:<10.2f} {p[3]:<10}")
            else:
                print("\n⚠️ No hay productos registrados.")
            funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "REALIZAR VENTA":
            funciones.borrarPantalla()
            print("\n\t..:: Realizar Venta ::..")
            productos = produc.obtener_productos()
            if productos:
                 print("\n📦 PRODUCTOS DISPONIBLES:")
                 print(f"\n{'ID':<5}{'Nombre':<20}{'Precio':<10}{'Stock':<10}")
                 print("-" * 45)
                 for p in productos:
                     print(f"{p[0]:<5}{p[1]:<20}${p[2]:<9.2f}{p[3]:<10}")
                 print("-" * 45)
            venta_id_grupo = random.randint(1000, 9999)
            continuar_venta = True

            while continuar_venta:
                producto_id = input("\tID del producto (o 'X' para terminar): ").strip()
                if producto_id.upper() == "X":
                    break

                producto = produc.buscar_producto_por_id(producto_id)
                if producto:
                    nombre_prod = producto[1]
                    precio_unitario = producto[2]
                    stock = producto[3]

                    print(f"\n🔎 Producto: {nombre_prod}")
                    print(f"💵 Precio unitario: ${precio_unitario:.2f}")
                    print(f"📦 Stock disponible: {stock}")

                    try:
                        cantidad = int(input("\n📥 Cantidad a vender: "))
                    except ValueError:
                        print("\n⚠️ Cantidad inválida.")
                        continue

                    if cantidad <= 0:
                        print("\n⚠️ La cantidad debe ser mayor que cero.")
                    elif cantidad > stock:
                        print("\n⚠️ Stock insuficiente.")
                    else:
                        total = cantidad * precio_unitario
                        print(f"\n💰 Total: ${total:.2f}")
                        confirmar = input("¿Confirmar venta? (s/n): ").lower()
                        if confirmar == "s":
                            ventas.registrar_venta(venta_id_grupo, usuario_id, producto_id, cantidad, precio_unitario)
                            produc.actualizar_stock(producto_id, -cantidad)
                            print("\n✅ Venta realizada.")
                        else:
                            print("\n⛔ Venta cancelada.")
                else:
                    print("\n⚠️ Producto no encontrado.")

                otra = input("\n¿Deseas vender otro producto? (s/n): ").lower()
                if otra != "s":
                    continuar_venta = False

            resumen = ventas.obtener_venta_por_grupo(venta_id_grupo)
            if resumen:
                print(f"\n🧾 Ticket de Venta (ID Grupo: {venta_id_grupo})")
                print(f"{'Producto':<20}{'Cantidad':<10}{'P.Unit':<10}{'Subtotal':<10}")
                print("-" * 60)
                total_general = 0
                for r in resumen:
                 subtotal = r[1] * r[2]
                 total_general += subtotal
                 print(f"{r[0]:<20}{r[1]:<10}{r[2]:<10.2f}{subtotal:<10.2f}")
                 print("-" * 60)
                 print(f"{'TOTAL GENERAL:':<40}${total_general:.2f}")
            else:
                print("\n⚠️ No hay productos en esta venta.")
            funciones.esperarTecla()

        elif opcion == "4" or opcion.upper() == "HISTORIAL DE VENTAS":
           funciones.borrarPantalla()
           print("\n1️⃣ Mi historial de ventas")
           print("2️⃣ Historial completo de ventas")
           sub_opcion = input("\nSeleccione una opción: ").strip()
           if sub_opcion == "1":
               ventas_usuario = ventas.obtener_historial(usuario_id)
               if ventas_usuario:
                   print(f"\n🧾 Historial de Ventas de: {nombre}")
                   print(f"\n{'ID':<5}{'Producto':<20}{'Cantidad':<10}{'Total':<10}{'Fecha':<20}")
                   print("-" * 65)
                   total_usuario = 0
                   for v in ventas_usuario:
                       print(f"{v[0]:<5}{v[1]:<20}{v[2]:<10}{v[3]:<10.2f}{v[4]}")
                       total_usuario += v[3]
                   print("-" * 65)
                   print(f"\n💰 Total vendido por {nombre}: ${total_usuario:.2f}")
               else:
                   print("\n⚠️ No tienes ventas registradas.")
           elif sub_opcion == "2":
                ventas_completas = ventas.obtener_historial_completo()
                if ventas_completas:
                    print("\n🧾 HISTORIAL COMPLETO DE VENTAS")
                    print(f"\n{'ID':<5}{'Usuario':<20}{'Producto':<20}{'Cant':<10}{'Total':<10}{'Fecha':<15}")
                    print("-" * 85)
                    total_general = 0
                    for v in ventas_completas:
                        print(f"{v[0]:<5}{v[1]:<20}{v[2]:<20}{v[3]:<10}{v[4]:<10.2f}{v[5]:<15}")
                        total_general += v[4]
                    print("-" * 85)
                    print(f"\n💰 TOTAL GENERAL VENDIDO: ${total_general:.2f}")
                else:
                    print("\n⚠️ No hay ventas registradas en el sistema.")
           from datetime import date
           hoy = str(date.today())
           ventas_dia = ventas.obtener_ventas_del_dia(hoy)
           if ventas_dia:
               if sub_opcion == "1":
                   total_dia = sum(float(v[3]) for v in ventas_dia if isinstance(v[3], (int, float)))
               else:
                   total_dia = sum(float(v[4]) for v in ventas_dia if isinstance(v[4], (int, float)))
           else:
                total_dia = 0
           print(f"\n📆 Corte de caja del día {hoy}: ${total_dia:.2f}")
           funciones.esperarTecla()


        elif opcion == "5" or opcion.upper() == "ELIMINAR PRODUCTO":
            funciones.borrarPantalla()
            print("\n\t..:: Eliminar Producto ::..")
            productos = produc.obtener_productos()
            if productos:
                 print("\n📦 PRODUCTOS DISPONIBLES:")
                 print(f"\n{'ID':<5}{'Nombre':<20}{'Precio':<10}{'Stock':<10}")
                 print("-" * 45)
                 for p in productos:
                     print(f"{p[0]:<5}{p[1]:<20}${p[2]:<9.2f}{p[3]:<10}")
                 print("-" * 45)
            producto_id = input("\tID del producto a eliminar: ").strip()
            confirmado = input("\t¿Estás seguro de eliminarlo? (s/n): ").lower()

            if confirmado == "s":
                try:
                    eliminado = produc.eliminar_producto(producto_id)
                    if eliminado:
                        print("\n✅ Producto eliminado correctamente.")
                    else:
                        print("\n⚠️ El producto no pudo ser eliminado (puede que ya haya sido vendido).")
                except Exception as e:
                    print(f"\n⚠️ Error al eliminar producto: {e}")
            funciones.esperarTecla()

        elif opcion == "6" or opcion.upper() == "EXPORTAR INVENTARIO":
            funciones.borrarPantalla()
            print("\n\t.:: 🔍 Exportar inventario 🔍 ::. \n")
            datos, columnas = produc.exportar_inventario()
            
            if datos:
                op = True
                while op:
                    expo = input("¿Deseas exportar el inventario en Excel? (Si/No): ").upper().strip()
                    
                    if expo == "SI":
                        archivo = produc.generar_excel(datos, columnas)
                        if archivo:
                            print(f"\n✅ Inventario exportado correctamente:\n{archivo}")
                        else:
                            print("\n❌ Error al exportar el inventario")
                        op = False
                        
                    elif expo == "NO":
                        print("\n⛔ Exportación cancelada")
                        op = False
                        
                    else:
                        print("\n⚠️ Opción no válida. Intente nuevamente.")
            else:
                print("\n⚠️ No hay productos en el inventario para exportar.")
            
            funciones.esperarTecla()
            funciones.esperarTecla()
        elif opcion == "7" or opcion.upper() == "CERRAR SESION":
            print(f"\n👋 Cerrando sesión de {nombre}...")
            break

        else:
            print("\n⚠️ Opción inválida.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()
