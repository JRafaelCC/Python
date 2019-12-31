# JUEVES 19, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: IMPRIMIR EL SUELDO DE UN TRABAJADOR...
# PEDIR EL NOMBRE, LAS HORAS TRABAJADAS, HORAS EXTRAS.
# COSTO POR HORA = 123.3, IMPUESTOS = 35% DEL SUELDO BASE
# PAGAR HORAS EXTRAS 1.5 SUPERIOR QUE LO NORMAL

print("Sueldo de trabajador")

while True:

    def imprimir():  # POR QUE IMPRIME LOS VALORES SI NO LOS ESTA RECIBIENDO???
        print("\n****************************************")
        print("Trabajador: ", nombre)
        print("El costo por hora es: ", costo_h)
        print("Las horas trabajadas son: ", ht)
        print("El sueldo base es: ", sueldo_b)
        print("Los impuestos son: ", impuestos)
        print("***************************************")
        print("Total a pagar: ", total_p, "\n")

    nombre = str(input("\nNombre del trabajador: "))
    ht = float(input("Ingrese las horas trabajadas: "))

    costo_h = 123.3
    he = ht-40

    if he != 0:
        sueldo_b = ht * costo_h * 1.5
        impuestos = .35 * sueldo_b
        total_p = sueldo_b - impuestos
        imprimir()

    else:
        sueldo_b = ht * costo_h
        impuestos = .35 * sueldo_b
        total_p = sueldo_b - impuestos
        imprimir()

    rep = input("\nDesea repetir el programa Si/No: ")
    if rep == "No" or rep == "no":
        print("\nHasta luego")
        break
