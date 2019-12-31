# MIERCOLES 25, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PEDIR 2 MATRICES E IMPRIMIR LA SUMA

import numpy as np

print("\nSuma de matrices!!")

while True:

    matriz1 = []
    matriz2 = []
    print("\nPrimer matirz")
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrege el numero de columnas: "))
    for i in range(0, filas):
        matriz1.append([])
        for j in range(0, columnas):
            valor = float(input(f"Valor en la posicion {i, j}: "))
            matriz1[i].append(valor)
            valor = 0
    for i in range(0, filas):
        print(matriz1[i])
    print("\nSegunda matirz")
    for i in range(0, filas):
        matriz2.append([])
        for j in range(0, columnas):
            valor = float(input(f"Valor en la posicion {i, j}: "))
            matriz2[i].append(valor)
            valor = 0
    for i in range(0, filas):
        print(matriz2[i])
    suma = np.array(matriz1) + np.array(matriz2)
    print("\nLa suma de matrices es: \n", suma)

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "NO" or rep == "No" or rep == "no":
        print("\nHasta luego !")
        break
