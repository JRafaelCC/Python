# MIERCOLES 18, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: INGRESAR DOS NUMERO ENTEROS Y MOSTRAR LA SUMA, RESTA, MULTIPLICACION...
# DIVISION, DIVISION RESIDUO, SENO, COSENO, TANGENTE, ETC.

import math

print("\nOperaciones")

while True:

    a = int(input("\nIngrese el numero a: "))
    b = int(input("Ingrese el numero b: "))

    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    divresiduo = a % b
    expa = math.exp(a)
    expb = math.exp(b)
    raiza = math.sqrt(a)
    raizb = math.sqrt(b)
    sena = math.sin(a)
    senb = math.sin(b)
    cosa = math.cos(a)
    cosb = math.cos(b)
    tana = math.tan(a)
    tanb = math.tan(b)
    loga = math.log(a, 10)
    logb = math.log(b, 10)
    p = math.pow(a, b)

    print("\nLa suma de a+b es:", suma)
    print("La resta de a-b es:", resta)
    print("El producto de a*b es:", mult)
    print("La division de a/b es:", div)
    print("El residuo de la division de a%b es:", divresiduo)
    print("Exponencial, a:", expa, " b:", expb)
    print("Raiz, a:", raiza, " b:", raizb)
    print("Seno, a:", sena, " b:", senb)
    print("Coseno, a:", cosa, " b:", cosb)
    print("Tangente, a:", tana, " b:", tanb)
    print("Logaritmo base 10, a:", loga, " b:", logb)
    print(p)

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no":
        print("\nHasta luego")
        break
