# VIERNES 20, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: INGRESAR UN NUMERO E IMPRIMIR SU TABLA DE MULTIPLICAR

print("\nTabla de multiplicar!!")

while True:

    ciclo_for = ["F", "f", "1"]
    ciclo_while = ["W", "w", "2"]

    print("\nEliga el ciclo a utilizar: ")
    print(" For = ", ciclo_for, "\n", "While = ", ciclo_while)
    c = str(input("Ingrese el ciclo elegido: "))

    if c in ciclo_for:
        num = int(input("\nIngrese un numero: "))
        i = 1
        for i in range(1, 11):
            print("\t", num, "*", i, "= ", num*i)
            i = i + 1

    elif c in ciclo_while:
        num = int(input("\nIngrese un numero:"))
        i = 1
        while i in range(1, 11):
            print("\t", num, "*", i, "= ", num*i)
            i = i + 1

    else:
        print("\nVolver a intentar!")

    rep = str(input("\nDesea repetir el programa Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta luego!")
        break
