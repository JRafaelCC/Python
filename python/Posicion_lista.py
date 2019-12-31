# MIERCOLES 25, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PEDIR UNA SERIE DE NUMEROS
# IMPRIMIR EL MAYOR, MENOR Y LA POSICION EN LA QUE ESTAN

print("\nMayor y menor en la lista")

while True:

    lista = []

    ciclo_for = ["F", "f", "1"]
    ciclo_while = ["W", "w", "2"]

    print("\nEliga el ciclo a utilizar: ")
    print(" For = ", ciclo_for, "\n", "While = ", ciclo_while)
    c = str(input("Ingrese el ciclo elegido: "))

    if c in ciclo_for:
        tam = int(input("\nIngrese el tamaño de la lista: "))
        for i in range(0, tam):
            valor = int(input(f"Ingrese un valor en la posicion {i}: "))
            lista.append(valor)
            valor = 0
        print("\nLa lista es:", lista)
        posc = 0
        for j in range(0, tam):
            posc = lista[j]
            if posc == max(lista):
                print("\nEl valor mayor es:", posc, "en la posicion:", j)
    elif c in ciclo_while:
        tam = int(input("\nIngrese el tamaño de la lista: "))
        i = 0
        while i in range(0, tam):
            valor = int(input(f"Ingrese un valor en la posicion {i}: "))
            lista.append(valor)
            valor = 0
            i = i + 1
        print("\nLa lista es:", lista)
        posc = 0
        i = 0
        while i in range(0, tam):
            posc = lista[i]
            if posc == max(lista):
                print("\nEL valor mayor es:", posc, "en la posicion: ", i)
            i = i + 1
    else:
        print("Esa opcion no es valida!")

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "NO" or rep == "No" or rep == "no":
        print("\nHasta luego!!")
        break
