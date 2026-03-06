# Función que muestra el menú del programa
def mostrar_menu():
    print("\n=== MONEYFLY - CONTROLA TUS GASTOS HORMIGA ===")
    print("1. Registrar gasto")
    print("2. Ver gastos")
    print("3. Ver total gastado")
    print("4. Ver promedio de gastos")
    print("5. Salir")


def registrar_gasto(gastos):

    valor = float(input("Ingrese el valor del gasto: "))

    categoria = input("Ingrese la categoría del gasto: ")

    descripcion = input("Ingrese una breve descripción del gasto: ")

    gasto = {
        "valor": valor,
        "categoria": categoria,
        "descripcion": descripcion
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente")


def ver_gastos(gastos):

    if not gastos:
          print("Aún no has registrado gastos, ¡empieza ahora!")
          return
    print("\nLista de gastos:")

    for gasto in gastos:
            print(f"Valor: {gasto['valor']} | Categoria: {gasto['categoria']} | Descripción: {gasto['descripcion']}")


def calcular_total(gastos):

    if not gastos:
        print("No hay gastos registrados.")
        return

    total = sum(gasto["valor"] for gasto in gastos)
    print("Total gastado:", total)



def calcular_promedio(gastos):

    if not gastos:
        print("No hay gastos para calcular promedio")
        return

    total = sum(gasto["valor"] for gasto in gastos)

    promedio = total / len(gastos)

    print("Promedio de gastos:", promedio)



def main():

    # Lista gastos
    gastos = []

    
    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_gasto(gastos)

        elif opcion == "2":
            ver_gastos(gastos)

        elif opcion == "3":
            calcular_total(gastos)

        elif opcion == "4":
            calcular_promedio(gastos)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Oopss! Marca una opción válida")


# Punto de entrada del programa
if __name__ == "__main__":
    main()


