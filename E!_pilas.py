
pila = []

while True:
    print("\n--- MENU DE PILA ---")
    print("1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")

    opcion = int(input("Selecciona una opcion: "))

    match opcion:
        case 1:
            numero = int(input("Ingresa un numero: "))
            pila.append(numero)
            print("Numero agregado correctamente")

        case 2:
            if len(pila) > 0:
                print("Elemento eliminado:", pila.pop())
            else:
                print("La pila esta vacia")

        case 3:
            print("Pila actual:", pila)

        case 4:
            print("Programa terminado")
            break

        case _:
            print("Opcion no valida")
