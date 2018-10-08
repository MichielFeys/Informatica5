from math import sqrt

a = float(input('a: '))
b = float(input('b: '))

#berekeningen
c = sqrt((a ** 2) + (b ** 2))

#uitvoer
print('In een rechthoekige driehoek met rechthoekszijden a = ' + str(round(a, 2)) + ' en b = ' + str(round(b, 2)) + ' is de schuine zijde ' + str(round(c, 2)))