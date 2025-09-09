# Practica diagno_Angelo.py
# simulador de ticket de venta
# Objetivo: Aplicar funciones, bucles, condiciones.
# Listas y Variables

productos = ["Chetos", "Paleta de la rosa", "Mazapan", "Chicles", "Galletas", "Refrescos"]
precios = [15, 2.50, 4, 2, 6, 14]

# Función para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Programa principal
print("Bienvenido a la dulcería Candy")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("\nSelecciona tu pedido:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} quieres?: "))
    cantidades.append(cantidad)

# Calcular total
total = calcular_total(cantidades, precios)

# Mostrar ticket
print("\n------ TICKET DE COMPRA ------")
print(f"Cliente: {nombre}\n")
for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{productos[i]} x {cantidades[i]} = ${subtotal:.2f}")

print("------------------------------")
print(f"TOTAL A PAGAR: ${total:.2f}")
print("¡Gracias por su compra!")