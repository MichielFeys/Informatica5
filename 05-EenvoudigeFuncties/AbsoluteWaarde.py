x = float(input('x:'))
y = float(input('y:'))

#berekeningen
linker_lid = abs(abs(x) - abs(y))
rechter_lid = abs(x - y)
#uivoer
resultaat_a = round(linker_lid, 4)
resultaat_b = round(rechter_lid, 4)
#eind
print(str(resultaat_a) + ' ≤ ' + str(resultaat_b))


