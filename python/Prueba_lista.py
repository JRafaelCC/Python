# 23 LUNES, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBEMA: PEDIR UNA LISTA
# IMPRIMIR LA ORIGINAL Y CREAR OTRA CON LOS VALORES EN LA POSICION INVERSA

while True:

    lista_original = []
    lista_inversa = []

    tam = int(input("\nIngrese el tamano de la lista: "))
    print("\n")
    for i in range(0, tam):
        valor = int(input(f"Ingrese el valor del vector en la posicion {i}: "))
        lista_original.append(valor)
        valor = 0

    print("La lista original es:", lista_original)

    for i in range(0, tam):
        valor = lista_original[tam-1]-i
        lista_inversa.append(valor)
        valor = 0

    print("La lista inversa es:", lista_inversa)

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "NO" or rep == "No" or rep == "no":
        print("\nHasta luego!")
        break
