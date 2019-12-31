# JUEVES 19, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PEDIR EL NOMBRE DEL DESTINO, CUANTOS BOLETOS E IMPRIMIR EL COSTO EN PANTALLA

print("\nCosto de un vuelo!")

while True:

    def boleto(km: int, prod: int, des: str):
        costo = 10.75 * km * prod  # 10.75 pesos por km
        print("Destino: ", des)
        print("El costo del boleto es: ", float(costo))
        print("--------------------------------")

    print("\nLista de vuelos:")
    destinos = ["Guadalajara", "Yucatan", "Michoacan", "Oaxaca", "Colima"]

    for destino in destinos:
        print(destino)

    des = str(input("\nIngrese el destino deseado: "))
    prod = int(input("Ingrese el numero de boletos: "))

    print("\n--------------------------------")

    if des == "Guadalajara" or des == "guadalajara":
        km = 5
        boleto(km, prod, des)
    elif des == "Yucatan" or des == "yucatan":
        km = 300
        boleto(km, prod, des)
    elif des == "Michoacan" or des == "michoacan":
        km = 175
        boleto(km, prod, des)
        print("--------------------------------")
    elif des == "Oaxaca" or des == "oaxaca":
        km = 105
        boleto(km, prod, des)
    elif des == "Colima" or des == "colima":
        km = 65
        boleto(km, prod, des)
    else:
        print("\nEse destino no esta en la lista, vovler a intentar!")

    rep = str(input("\nDesea repetir el programa Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta luego!")
        break
