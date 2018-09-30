bedrag = int(input('Wat is uw bedrag?: '))
#berekeningen
aantal_munten = bedrag // 100
c = bedrag % 100
aantal_munten += (c // 50)
c %= 50
aantal_munten += (c // 20)
c %= 20
aantal_munten += (c // 10)
c %= 10
aantal_munten += (c // 5)
c %= 5
aantal_munten += (c // 2)
c %= 2
aantal_munten += (c // 1)
#uitvoer
print( str(bedrag) + ' cent kan je omwisselen in ' + str(aantal_munten) + ' muntstukken' )