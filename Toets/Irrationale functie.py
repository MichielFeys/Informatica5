
a = float(input('reëel getal a: '))


f = (a - 2) ** (1/2)


if a == 2:
    print('2.00 is nulpunt van f')
elif a < 2:
    print(str(a) + ' ∉' + ' dom(f)')
else:
    print('f(' + str(a) + ')' + ' = ' + str(round(f, 2)))