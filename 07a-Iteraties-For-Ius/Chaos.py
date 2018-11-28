d = float(input('bevolkingsaantal: '))
r = float(input('vruchtbaarheidsparameter: '))
s = int(input('aantal tijdsstappen: '))

t = 0
print(d)

for i in range(0, s-1):
    x = 0
    t += 1
    x += r*d*(1-d)
    d = x

    print(x)



