# LUNES 23, DIC, 2019
# CANTERO CARDENAS JOSE RAFAEL
# PROBLEMA: MANDAR A LLAMAR UN ARCHIVO .TXT

lista = open("Quinto.txt", "r")

print("\n")
for materia in lista:
    print(materia)

lista.close()
