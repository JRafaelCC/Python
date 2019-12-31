# 22 DOMINGO, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PEDIR EL TAMAÑO DE DOS VECTORES Y SUMARLOS

import numpy as np

print("\nSuma de vectores!")

while True:

    lista1 = []
    lista2 = []

    ciclo_for = ["F", "f", "1"]
    ciclo_while = ["W", "w", "2"]

    print("\nEliga el ciclo a utilizar: ")
    print(" For = ", ciclo_for, "\n", "While = ", ciclo_while)
    c = str(input("Ingrese el ciclo elegido: "))

    if c in ciclo_for:

        num = int(input("\nIngrese el tamaño de los vectores: "))
        print("\n")
        for e in range(0, num):
            valor = float(input(f"Valor del vector 1 en la posicion {e}: "))
            lista1.append(valor)
            valor = 0
        v1 = np.array(lista1)

        for e in range(0, num):
            valor = float(input(f"Valor del vector 2 en la posicion {e}: "))
            lista2.append(valor)
            valor = 0
        v2 = np.array(lista2)

        print("\nVector 1: ", v1.astype(float))
        print("Vector 2: ", v2.astype(float))
        print("La suma es:", v1.astype(float)+v2.astype(float))
    elif c in ciclo_while:

        num = int(input("\nIngrese el tamaño de los vectores: "))
        print("\n")
        e = 0
        while e in range(0, num):
            # NO ACEPTA MAS DE DOS ARGUMENTOS
            valor = float(input(f"Valor del vector 1 en la posicion {e}: "))
            lista1.append(valor)
            valor = 0
            e = e + 1
        v1 = np.array(lista1)
        e = 0
        while e in range(0, num):
            valor = float(input(f"Valor del vector 2 en la posicion {e}: "))
            lista2.append(valor)
            valor = 0
        e = e + 1
        v2 = np.array(lista2)

        print("\nVector 1: ", v1.astype(float))
        # NO ME PERMITE IMPRIMIR CON ALGUN TEXTO O CON LA SUMA DIRECTA DE V1 Y V2
        print("Vector 2:", v2.astype(float))
        print("La suma es:", v1.astype(float)+v2.astype(float))
    else:
        print("Vuelve a intentar!!")

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no" or rep == "NO":
        print("\nHasta luego!")
        break
