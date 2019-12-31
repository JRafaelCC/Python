# VIERNES 20, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: IMPRIMIR EL ABECEDARIO
# PEDIR SI ES ASCENDENTE O DESCENDENTE

print("\nAbecedario!")

asc = ["Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Gg", "Hh", "Ii", "Jj", "Kk", "Ll", "Mm", "Nn",
       "Oo", "Pp", "Qq", "Rr", "Ss", "Tt", "Uu", "Vv", "Ww", "Xx", "Yy", "Zz"]
desc = ["Zz", "Yy", "Xx", "Ww", "Vv", "Uu", "Tt", "Ss", "Rr", "Qq", "Pp", "Oo", "Nn", "Mm",
        "Ll", "Kk", "Jj", "Ii", "Hh", "Gg", "Ff", "Ee", "Dd", "Cc", "Bb", "Aa"]

while True:

    print("\nEliga con que ciclo se realizara: ")
    ciclos = ["F, f, 1 = For", "W, w, 2 = While"]
    f = ["1", "F", "f"]
    w = ["2", "W", "w"]
    for ciclo in ciclos:
        print(ciclo)

    c = input("Ingrese el ciclo elegido: ")

    if c in f:               # in == "F" or c == "f" or c == "1":
        dir = input("\nEliga ascendente o descendente a/d: ")
        if dir == "a":
            for caracter in asc:
                print(caracter)

        elif dir == "d":
            for caracter in desc:
                print(caracter)

    elif c in w:
        dir = input("\nEliga ascendente o descendente a/d: ")
        if dir == "a":
            i = 0
            while i != len(asc):
                caracter = asc[i]
                print(caracter)
                i = i + 1

        if dir == "d":
            asc.reverse()
            print(asc)
            i = 0
            while i != len(desc):
                caracter = desc[i]
                print(caracter)
                i = i + 1

    else:
        print("Volver a intentarlo!")

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no":
        print("\nHasta luego")
        break
