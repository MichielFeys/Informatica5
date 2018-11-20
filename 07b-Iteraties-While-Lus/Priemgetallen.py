getal = int(input('getal: '))
n = 2
i = 1
while n < getal:
    if (getal % n) == 0:
        antw = '{} is geen priemgetal'.format(getal)
        i = 0
    n += 1
if i and getal != 1:
    antw = '{} is een priemgetal'.format(getal)
elif getal == 1:
    antw = '1 is geen priemgetal'

print(antw)