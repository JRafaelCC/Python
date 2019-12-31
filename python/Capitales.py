# VIERNES 20, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: PREGUNTAR LA CAPITAL DE LOS ESTADOS DE MEXICO

import random
print("\nBienvenido, empecemos!!")

capitales = {
    'Aguascalientes': 'Aguascalientes',
    'Baja California': 'Mexicali',
    'Baja California Sur': 'La Paz',
    'Campeche': 'San Francisco de Campeche',
    'Chihuahua': 'Chihuahua',
    'Ciudad de Mexico': 'Ciudad de Mexico',
    'Chiapas': 'Tuxtla Gutierrez',
    'Coahuila': 'Saltillo',
    'Colima': 'Colima',
    'Durango': 'Victoria de Durango',
    'Guanajuato': 'Guanajuato',
    'Guerrero': 'Chilpancingo',
    'Hidalgo': 'Pachuca de Soto',
    'Jalisco': 'Guadalajara',
    'Mexico DF': 'Toluca de Lerdo',
    'Michoacan': 'Morelia',
    'Morelos': 'Cuernavaca',
    'Nayarit': 'Tepic',
    'Nuevo Leon': 'Monterrey',
    'Oaxaca': 'Oaxaca de Juarez',
    'Puebla': 'Puebla de Zaragoza',
    'Queretaro': 'Santiago de Queretaro',
    'Quintana Roo': 'Chetumal',
    'San Luis Potosi': 'San Luis Potosi',
    'Sinaloa': 'Culiacan Rosales',
    'Sonora': 'Hermosillo',
    'Tabasco': 'Villa Hermosa',
    'Tamaulipas': 'Ciudad Victoria',
    'Tlaxcala': 'Tlaxcala',
    'Veracruz': 'Xalapa Enriquez',
    'Yucatan': 'Merida',
    'Zacatecas': 'Zacatecas'
}


estados = list(capitales.keys())

while True:

    def num_random():
        estado = random.choice(estados)
        capital = capitales[estado]
        resp = str(input("\n¿ Cual es la capital de "+estado+" ? "))
        if resp == capital:
            print("Correcto!")
        else:
            print("Incorrecto!")

    ciclo_for = ["F", "f", "1"]
    ciclo_while = ["W", "w", "2"]

    print("\nEliga un ciclo a utilizar:  ")
    print(" For =", ciclo_for, "\n", "While =", ciclo_while)
    c = str(input("¿Que ciclo desea utilizar? "))

    if c in ciclo_for:
        for i in range(1, 4):   # [1, 2, 3]
            num_random()

    elif c in ciclo_while:
        i = 1
        while i in range(1, 4):
            num_random
            i = i + 1

    rep = str(input("\nDesea repetir el juego Si/No: "))
    if rep == "No" or rep == "no":
        print("\nHasta pronto!")
        break
