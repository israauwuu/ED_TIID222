matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

matriz.append([39, 22, 69, 17])
for i in range(len(matriz[1])):
    print(matriz[1][i])

for i in matriz:
    if 61 in i:
        print(f"61 encontrado en la fila (i)")
        break

for filas in matriz:
    for numeros in filas:
        if numeros == 18:
            print(f"18 encontado en la filas(filas)")
            break 