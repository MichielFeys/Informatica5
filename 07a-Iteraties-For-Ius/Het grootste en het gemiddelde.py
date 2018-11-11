aantal_getallen = int(input('Aantal getallen: '))


max = 0
som = 0

for i in range(aantal_getallen):
    getal = int(input('getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

gem = (som / aantal_getallen)


print('Het grootste getal is ' + str(max) +' en het gemiddelde is ' + '{:.2f}'.format(gem))