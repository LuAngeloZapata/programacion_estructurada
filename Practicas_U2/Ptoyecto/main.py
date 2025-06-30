import Puntoventa
def menu():
    ventas = []
    datos = []
    opcion = True
    nombre_usuario = None
    while not nombre_usuario:
        Puntoventa.BorrarPantalla()
        nombre_usuario = Puntoventa.Usuario_password()
    while opcion:
        Puntoventa.BorrarPantalla()
        opcion= Puntoventa.Menu_Principal(nombre_usuario)
        match opcion:
            case "1":
                Puntoventa.AgregarProducto(datos)
                Puntoventa.EsperarTecla()
            case "2":
                Puntoventa.Inventario(datos)
                Puntoventa.EsperarTecla()
            case "3":
                Puntoventa.VenderProducto(datos, ventas)
                Puntoventa.EsperarTecla()
            case "4":
                Puntoventa.HistorialVenta(ventas)
                Puntoventa.EsperarTecla()
            case "5":
                Puntoventa.BorrarProducto(datos)
                Puntoventa.EsperarTecla()
            case "6":
                Puntoventa.Usuario_password()    
            case "7":
                opcion = False
                print("\n\t Terminaste de ejecutar el programa")
                print("\n\t  Hasta la proxima")
            case _:
                input("\n\t Opcion invalida: Precione enter para continuar")
if __name__ == "__main__":
    menu()                



