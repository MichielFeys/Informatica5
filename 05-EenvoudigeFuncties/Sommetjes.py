#input
a = int(input('a, tussen 0 en 20: '))
b = int(input('b, tussen 0 en 20: '))

#berekeningen
uitvoer_a = (a * 10 ** 0)
uitvoer_b = (a * 10 ** 1)
uitvoer_c = (a * 10 ** 2)
uitvoer_d = (a * 10 ** 3)
uitvoer_e = (a * 10 ** 4)
uitvoer_aa = (b * 10 ** 0)
uitvoer_bb = (b * 10 ** 1)
uitvoer_cc = (b * 10 ** 2)
uitvoer_dd = (b * 10 ** 3)
uitvoer_ee = (b * 10 ** 4)

#uitvoer
print('{:6d}'.format(uitvoer_a) + ' + ' + '{:<6d}'.format(uitvoer_aa) + ' = ' + str(uitvoer_a + uitvoer_aa))
print('{:6d}'.format(uitvoer_b) + ' + ' + '{:<6d}'.format(uitvoer_bb) + ' = ' + str(uitvoer_b + uitvoer_bb))
print('{:6d}'.format(uitvoer_c) + ' + ' + '{:<6d}'.format(uitvoer_cc) + ' = ' + str(uitvoer_c + uitvoer_cc))
print('{:6d}'.format(uitvoer_d) + ' + ' + '{:<6d}'.format(uitvoer_dd) + ' = ' + str(uitvoer_d + uitvoer_dd))
print('{:6d}'.format(uitvoer_e) + ' + ' + '{:<6d}'.format(uitvoer_ee) + ' = ' + str(uitvoer_e + uitvoer_ee))