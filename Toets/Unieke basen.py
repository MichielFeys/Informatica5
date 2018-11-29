x = int(input('hoeveel basen: '))
hoeveelheid_basen = 0
basen = ''
for i in range(x):
    y = input('base: ')
    if y not in basen:
        basen += y
for len in basen:
    hoeveelheid_basen += 1


print('De DNA-keting bevat ' + str(hoeveelheid_basen) + ' verschillende soorten basen: {}'.format(basen))