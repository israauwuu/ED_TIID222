arreglo = []

for i in range (5):

    dato=int(input("Ingrese un numero: "))

    if(dato>=0 and dato<=500):
        arreglo.append(dato)
    else:
        print("El numero ingresado no es valido")

arregloCinuerizado = []

for i in range (5):
    if(arreglo[i]%5==0):
        arregloCinuerizado.append(arreglo[i])

    else:
        arregloCinuerizado.append(arreglo[i]+(5-arreglo[i]%5))

print("El arreglo original es: ",arreglo)
print("El arreglo cincuerizado es: ",arregloCinuerizado)

    




        
        

    
    


