
from collections import deque

cola = deque()

while True:
    print("\n--- MENU DE COLA ---")
    print("1. Insertar en cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")

    opcion = int(input("Selecciona una opcion: "))

    match opcion:
        case 1:
            numero = int(input("Ingresa un numero: "))
            cola.append(numero)
            print("Numero agregado correctamente")

        case 2:
            if len(cola) > 0:
                print("Elemento eliminado:", cola.popleft())
            else:
                print("La cola esta vacia")

        case 3:
            print("Cola actual:", list(cola))

        case 4:
            print("Programa terminado")
            break

        case _:
            print("Opcion no valida")
