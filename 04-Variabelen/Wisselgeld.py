bedrag = int(input('Wat is u bedrag?: '))

#gegeven
a = bedrag // 100
b = a // 50
c = b // 20
d = c // 10
e = d // 5
f = e // 2
g = f // 1

#berekening
muntstukken = str(int(a + b + c + d + e + f + g))
#uitvoer
print( str(bedrag) + ' kan je omwisselen in ' +  (str(muntstukken) ) + ' muntstukken' )