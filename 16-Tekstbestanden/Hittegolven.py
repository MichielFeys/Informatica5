temp = [28, 19, 26, 27, 23, 23, 25, 27, 30, 32, 25, 28]
lijnen = []
aantal_25_plus = 0
aantal_30_plus = 0
hittegolven = 0
for i in range(len(temp)):
    if aantal_25_plus >= 5 and aantal_30_plus >= 2:
        hittegolven += 1
        aantal_30_plus = 0
        aantal_25_plus = 0

    if temp[i] >= 30:
        aantal_30_plus += 1
        aantal_25_plus += 1

    if temp[i] >= 25:
        aantal_25_plus += 1

    if temp[i] < 25:
        aantal_30_plus = 0
        aantal_25_plus = 0

print(hittegolven)

