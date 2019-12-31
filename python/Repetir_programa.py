# JUEVES 19, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# REALIZAR UN MENU DE OPERACIONES DONDE EL USUARIO PUEDA ELEGIR
# QUE EL PROGRAMA TENGA LA OPCION DE VOLVER A REPETIRSE

import math

while True:

    def valores():
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        return a, b

    def valor():
        a = float(input("Ingrese el numero a evaluar: "))

        return a

    print("\nEliga la operacion a realizar: ")
    operaciones = ["Suma, s, +", "Resta, r, -", "Multiplicacion, m, *", "División, d, /",
                   "Division (residuo), %", "Sin", "Cos", "Tangente", "Raiz", "Exponencial"]
    for operacion in operaciones:
        print(operacion)

    op = input("\nIngrese la operacion a realizar: ")

    if op == "Suma" or op == "s" or op == "+":
        a, b = valores()
        print("\nLa suma de ", a, "+", b, "= ", a+b)
    elif op == "Resta" or op == "r" or op == "-":
        a, b = valores()
        print("\nLa resta de ", a, "-", b, "= ", a-b)
    elif op == "Multiplicacion" or op == "m" or op == "*":
        a, b = valores()
        print("\nLa multiplicacion de ", a, "*", b, "= ", a*b)
    elif op == "Division" or op == "d" or op == "/":
        a, b = valores()
        print("\nLa division de ", a, "/", b, "= ", a/b)
    elif op == "Residuo" or op == "%":
        a, b = valores()
        print("\nEl residuo de ", a, "/", b, "= ", a % b)
    elif op == "Sin" or op == "seno":
        a = valor()
        print("\nEl sin(", a, ")= ", math.sin(a))
    elif op == "Cos" or op == "coseno":
        a = valor()
        print("\nEl cos(", a, ")= ", math.cos(a))
    elif op == "Tangente" or op == "tangente":
        a = valor()
        print("\nLa tan(", a, ")= ", math.tan(a))
    elif op == "Raiz" or op == "raiz":
        a = valor()
        print("\nLa raiz de ", a, "es: ", math.sqrt(a))
    elif op == "Exp" or op == "exp":
        a = valor()
        print("\nLa exp(", a, ")= ", math.exp(a))
    else:
        print("\nError, esa operacion no es valida")

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no":
        print("\nHasta luego!")
        break
