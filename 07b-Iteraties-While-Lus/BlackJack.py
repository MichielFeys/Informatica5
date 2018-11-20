kaart = int(input('kaart: '))
som = kaart

for i in range(1,11):
    while kaart > 0 and som < 21:
        kaart = int(input('kaart: '))
        som += kaart
        if som > 21:
            print('Verbrand (' + str(som) + ')')
        if som == 21:
            print('Gewonnen!')

if som < 21:
    print('Voorzichtig gespeeld (' + str(som) + ')')