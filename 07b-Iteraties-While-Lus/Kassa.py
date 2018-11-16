prijzen = float(input('prijs product : '))
som = prijzen
while prijzen > 0:
    prijzen = float(input('prijs product: '))
    som += prijzen


print('De totale prijs is € {:.2f}'.format(som))