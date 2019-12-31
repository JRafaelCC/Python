# MIERCOLES 18, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: INGRESAR UN NUMERO Y EVALUAR SI ES PAR O INPAR

print("\nIdentificar PAR o INPAR")

while True:

    def resultado():
        num = int(input("\nIngrese un numero a evaluar: "))
        return num

    res = resultado()

    if (res % 2) == 0:
        print("\nEl numero", res, "es PAR\n")
    else:
        print("\nEl numero", res, "es INPAR\n")

    rep = str(input("\nDesea repetir el programa Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta luego")
        break
