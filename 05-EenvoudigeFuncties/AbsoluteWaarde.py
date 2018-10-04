x = float(input('x:'))
y = float(input('y:'))

#berekeningen
linker_lid = abs(abs(x) - abs(y))
rechter_lid = abs(x - y)
#uivoer
uitvoer = float(round(4, linker_lid)) + '≤' + float(round(4, rechter_lid))
