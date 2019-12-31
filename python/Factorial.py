# JUEVES 19, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PEDIR UN ENTERO Y OBTENER SU FACTORIAL

while True:

    ciclo_for = ["F", "f", "1"]
    ciclo_while = ["W", "w", "2"]

    print("\nEliga el ciclo a utilizar: ")
    print(" For = ", ciclo_for, "\n", "While = ", ciclo_while)
    c = input("¿Que ciclo desea utilizar?: ")

    if c in ciclo_for:
        factorial = 1
        num = int(input("\nIngrese el numero a evaluar: "))
        a = 1
        for a in range(1, num):
            factorial = factorial * a
            a = a + 1
        print("El factorial de", num, "= ", factorial*num)
    elif c in ciclo_while:
        factorial = 1
        num = int(input("\nIngrese el numero a evaluar: "))
        a = 1
        while a in range(1, num):
            factorial = factorial * a
            a = a + 1
        print("El factorial de", num, "= ", factorial*num)
    else:
        print("\nVolver a intentar.")

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no":
        print("\nHasta luego")
        break
