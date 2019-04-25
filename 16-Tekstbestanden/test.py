# lijnen = []
#
# with open('klas.txt') as bestand:
#     lijnen = bestand.readlines()
#
#
# print('er zitten ' + str(len(lijnen)) + ' personen in de klas')

nieuwe_leerlingen= ['Alice', 'Baptistje autistje']

with open('klas.txt', 'w') as bestand:
    bestand.write('\n' + '\n'.join(nieuwe_leerlingen))