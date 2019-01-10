def splits(getal):
    getal = int(getal)
    getal1 = int(getal/1000)
    getal2 = int((getal - getal1*1000) / 100)
    getal3 = int((getal-getal1*1000-getal2*100) / 10)
    getal4 = int(getal - getal1 * 1000 - getal2 * 100 - getal3 * 10)

    return getal1, getal2, getal3, getal4

def oplopende_cijfers(g1, g2, g3, g4):
    alle_getallen = g1, g2, g3, g4
    bewerking = tuple(sorted(alle_getallen))
    return bewerking

def op_af_getallen(a, b, c, d):
    op_rij = ''
    af_rij = ''
    op_rij += str(a) + str(b) + str(c) + str(d)
    af_rij += str(d) + str(c) + str(b) + str(a)
    return op_rij, af_rij

def verschil(x, y):
    verschl = str(int(x) - int(y))
    return verschl


def largest(nstr):
    if (len(nstr) == 0):
        return ""
    elif (len(nstr) == 4) and (nstr[0] == nstr[1] == nstr[2] == nstr[3]):
        return "7641"
    digit = -1
    index = 0
    for i in range(0, len(nstr)):
        if (digit < int(nstr[i])):
            digit = int(nstr[i])
            index = i
    return str(digit) + largest(nstr[0:index] + nstr[index + 1:len(nstr)])


def kaprekar(n):
    mes =''
    a = n // 1000
    b = (n - (a * 1000)) // 100
    c = (n - (a * 1000) - (b * 100)) // 10
    d = n - (a * 1000) - (b * 100) - (c * 10)
    g1 = min(a, b, c, d)
    g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
    g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
    g4 = max(a, b, c, d)
    oprij = str(g1) + str(g2) + str(g3) + str(g4)
    afrij = str(g4) + str(g3) + str(g2) + str(g1)
    if int(afrij) - int(oprij) == 6174:
        mes = '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    else:

        while int(afrij) - int(oprij) != 6174:
            mes += '{} - {} = {}\n'.format(afrij, oprij, int(afrij) - int(oprij))
            n = int(afrij) - int(oprij)
            a = n // 1000
            b = (n - (a * 1000)) // 100
            c = (n - (a * 1000) - (b * 100)) // 10
            d = n - (a * 1000) - (b * 100) - (c * 10)
            g1 = min(a, b, c, d)
            g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
            g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
            g4 = max(a, b, c, d)
            oprij = str(g1) + str(g2) + str(g3) + str(g4)
            afrij = str(g4) + str(g3) + str(g2) + str(g1)
        a = n // 1000
        b = (n - (a * 1000)) // 100
        c = (n - (a * 1000) - (b * 100)) // 10
        d = n - (a * 1000) - (b * 100) - (c * 10)
        g1 = min(a, b, c, d)
        g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
        g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
        g4 = max(a, b, c, d)
        oprij = str(g1) + str(g2) + str(g3) + str(g4)
        afrij = str(g4) + str(g3) + str(g2) + str(g1)
        mes += '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    return mes