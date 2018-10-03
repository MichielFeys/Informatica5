sol = int(input('Aantal sol:'))

#geveven
een_sol = 24.65979
een_dag = 24

#berekenignen
x = een_sol * sol

aantal_dagen = int(x // 24)
x %= 24
aantal_uren = int(x // 1)
x %= 1
aantal_minuten = int(x // 0.016666666666666666 )
x %= 0.016666666666666666
aantal_seconden = int(x // 0.0002777777777777778)


#uitvoer
print( str(sol) + ' sol = ' + str(aantal_dagen) + ' dagen, ' + str(aantal_uren) + ' uren, ' + str(aantal_minuten) + ' minuten en ' + str(aantal_seconden) + ' seconden')