def mostrar_menu():
    print=("\n===MONEYFLY - CONTROL DE TUS GASTOS HORMIGA===")
    print=("1.Registro gasto")
    print=("2. Ver gastos")
    print=("3. Ver total gastado")
    print=("4. Ver promedio de gastos")
    print=("5. Salir")

def main():
    gastos = []

while True:
    mostrar_menu()
    opcion = input("Hola! :) Seleccione una opción: ").strip()
    if opcion == "1":
        print("Registrar gasto(pdte)")
    elif opcion == "2":
        print ("Ver gastos(pdte)")
    elif opcion == "3":
        print ("Ver total(pdte)")
    elif opcion == "4":
        print ("Ver promedio")
    elif opcion == "5":
        print ("Salir...")
        break
    else: 
        print("¡Ooops! Marca una opción válida")

    if __name__ == "__main__":
         main()



