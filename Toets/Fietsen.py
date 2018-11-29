s = int(input('snelheid stijn: '))
k = int(input('snelheid kaat: '))
m = int(input('afstand: '))
t = 0

while m > 0:
    t += 1
    m -= s + k

print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(t))