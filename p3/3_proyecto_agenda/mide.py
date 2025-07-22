import agenda

def main():
    opcion = True
    while opcion:
        agenda.borrarPantalla()
        opcion = agenda.menu_Principal()
        match opcion:
            case "1":
                agenda.AgregarContactos()
                agenda.esperarTecla()
            case "2":
                agenda.MostrarContactos()
                agenda.esperarTecla()
            case "3":
                agenda.BuscarContactos()
                agenda.esperarTecla()
            case "4":
                agenda.ModificarContacto()
                agenda.esperarTecla()
            case "5":
                agenda.EliminarContacto()
                agenda.esperarTecla()
            case "6":
                print("\n👋 Programa finalizado.")
                opcion = False
            case _:
                input("❌ Opción inválida. Presiona Enter para intentar de nuevo.")

if __name__ == "__main__":
    main()
