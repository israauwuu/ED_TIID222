#Declarando arreglo
numeros = [10,20,30,40,50]

#Imprimimos un elemento especifico del arreglo
print(numeros[2])

#Reasignamos un valor en una posicion especifica
numeros[3] = 35
print(numeros)

#Agregamos un nuevo valor al arreglo
numeros.append(60)
print(numeros)

#Eliminamos un valor del arreglo
numeros.remove(35)
print(numeros)

#Eliminamos una posicion del arreglo
numeros.pop(4)
print(numeros)

#Creamos otro arreglo de texto
frutas = ["Manzana", "Fresq", "sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)

frutas.remove("Manzana")
print(frutas)