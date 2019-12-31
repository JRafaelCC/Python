# MIERCOLES 18, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: CALCULAR EL AREA DE UN TRIANGULO

print("\nArea de un triangulo!!")

while True:

    def area_triangulo(b, h):
        a = (b*h)/2
        return a

    b = float(input("\nIngrese el valor de la base: "))
    h = float(input("Ingrese el valor de la altura: "))

    area = area_triangulo(b, h)

    print("\nEl area del triangulo es:", area)

    rep = str(input("\nDesea repetir el programa Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta luego!")
        break
