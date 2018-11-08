d_v = float(input('De verkeersdichtheid van het vrachtvervoer op het eerste rijvak: '))
v_v = float(input('De snelheid van het vrachtverkeer op het eerste rijvak: '))
d_a = float(input('De verkeersdichtheid van het personenvervoer op het tweede rijvak: '))
v_a = float(input('De snelheid van de personenwagens op het tweede rijvak: '))

x = (v_a * d_a) / 40
y = (v_v * d_v) / 40
n = float(0.7)
p_a = min(x, 1)
p_v = min(y, 1)

if min(p_a,p_v) >= n:
    print('zwart')
elif max(p_a, p_v) > n and (p_v - p_a) < n:
    print('rood')
elif and (p_v - p_a) < n:
    print('c')
elif (p_v - p_a) > n:
    print('geel')
else:
    print('groen')