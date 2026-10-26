#clase que representa a un nodo
class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

#clase que administra todos los nodos de las listas enlazadas
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_nodo_al_inicio(self, numero):
        #crea un nuevo nodo con el numero recibido
        nuevo_nodo=Nodo(numero)

        #comprobar si la lista esta vacia 
        if(self.cabeza is None):

            #vamos a pasar el  nuevo nodo en nuestra cabeza
            self.cabeza=Nodo(numero)

            return
        #si la lista ya tenia nodos, el nuevo nodo apunta al que era la cabeza
        nuevo_nodo.siguiente = self.cabeza

        #actualizar nuestra cabeza para que apunte al nuevo nodo
        self.cabeza = nuevo_nodo

    #metodo para insertar nodo al final de la lista
    def insertar_nodo_al_final(self, numero):

        #creamos nuevo nodo con el numero que se recibe
        nuevo_nodo=Nodo(numero)

        #comprobamos si esta vacia
        if(self.cabeza is None):

            #si la lista esta vacia, el nuevo nodo sera el primero
            self.cabeza=Nodo(numero)
            return

        #referencia temporal al primer nodo
        actual=self.cabeza

        #avanzar mientras exista un nodo siguiente
        while(actual.siguiente):

            #mi actual pasa a ser el actual.siguiente
            actual=actual.siguiente

        #cuando ya no hay uno siguiente conecta al nuevo nodo
        actual.siguiente=nuevo_nodo

    #metodo para imprimir nuestra lista enlazada 
    def imprimir_ListaEnlazada(self):
        actual = self.cabeza

        while(actual):

            #imprimimos nuestra lista
            print(actual.numero, "→" , end=" ")

            #avanzamos al siguiente nodo y ahora sera e actual
            actual=actual.siguiente

        print("None")


Mi_lista = ListaEnlazada()
Mi_lista.insertar_nodo_al_inicio(2)
Mi_lista.insertar_nodo_al_inicio(3)
Mi_lista.insertar_nodo_al_final(4)
Mi_lista.imprimir_ListaEnlazada()
            