# JUEVES 19, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: CREAR UN MENU CON 10 OPERACIONES
# DONDE EL USUARIO ELIGA LA OPERACION

import math

print("\nCalculadora")

while True:

    def valores():
        a = float(input("\nIngrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        return a, b

    def valor():
        a = float(input("\nIngrese el numero a evaluar: "))
        return a

    print("\nEliga la operacion a realizar: ")
    operaciones = ["Suma, s, +", "Resta, r, -", "Multiplicacion, m, *", "División, d, /",
                   "Division (residuo), %", "Sin", "Cos", "Tangente", "Raiz", "Exponencial"]
    for operacion in operaciones:
        print(operacion)

    op = str(input("\nTecle la operacion a realizar: "))

    if op == "Suma" or op == "s" or op == "+":
        a, b = valores()
        print("La suma de ", a, "+", b, "=", a+b)
    elif op == "Resta" or op == "r" or op == "-":
        a, b = valores()
        print("La resta de ", a, "-", b, "=", a-b)
    elif op == "Multiplicacion" or op == "m" or op == "*":
        a, b = valores()
        print("La multiplicacion de ", a, "*", b, "=", a*b)
    elif op == "Division" or op == "d" or op == "/":
        a, b = valores()
        print("La division de ", a, "/", b, "=", a/b)
    elif op == "Residuo" or op == "%":
        a, b = valores()
        print("El residuo de ", a, "/", b, "=", a % b)
    elif op == "Sin":
        a = valor()
        print("El sin(", a, "): ", math.sin(a))
    elif op == "Cos":
        a = valor()
        print("El cos(", a, "): ", math.cos(a))
    elif op == "Tangente":
        a = valor()
        print("La tan(", a, "): ", math.tan(a))
    elif op == "Raiz":
        a = valor()
        print("La raiz(", a, "): ", math.sqrt(a))
    elif op == "Exponencial":
        a = valor()
        print("La exp(", a, "): ", math.exp(a))
    else:
        print("\nLa operación ingresada no es posible")

    rep = str(input("\nDesea repetir el programa Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta luego!!")
        break
