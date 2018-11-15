n = int(input('Hoeveelste getal: '))

vorige = 1
huidige = 1

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige


print(huidige)
