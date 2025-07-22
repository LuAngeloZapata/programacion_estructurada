
import calificaciones

def main():
    opcion = True
    while opcion:
        calificaciones.borrarPantalla()
        print("\n\t\t📚 Sistema de Gestión de Calificaciones\n")
        print("1️⃣ - Agregar calificaciones")
        print("2️⃣ - Mostrar calificaciones")
        print("3️⃣ - Buscar alumno")
        print("4️⃣ - Modificar alumno")
        print("5️⃣ - Borrar alumno")
        print("6️⃣ - Salir")

        opcion = input("\nElige una opción: ").strip()

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones()
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones()
                calificaciones.esperarTecla()
            case "3":
                calificaciones.buscarAlumno()
                calificaciones.esperarTecla()
            case "4":
                calificaciones.modificarAlumno()
                calificaciones.esperarTecla()
            case "5":
                calificaciones.borrarAlumno()
                calificaciones.esperarTecla()
            case "6":
                print("\n👋 Programa terminado.")
                opcion = False
            case _:
                input("❌ Opción inválida. Presiona Enter para intentar de nuevo.")

if __name__ == "__main__":
    main()
