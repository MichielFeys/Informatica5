aantal_getallen = int(input('Aantal getallen: '))


max = int(input('getal: '))
som = max

for i in range(aantal_getallen - 1):
    getal = int(input('getal: '))
    som += getal
    if(getal > max):
        max = getal

gem = (som / aantal_getallen)


print('Het grootste getal is ' + str(max) +' en het gemiddelde is ' + '{:.2f}'.format(gem))