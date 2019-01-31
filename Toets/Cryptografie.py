def versleutel_woord(woord, n):
    nieuw_woord =''
    for i in range(0, len(woord)):
        hoofdletters = woord[i].upper
        nieuw_woord += woord[i].upper()
        if n < 32:
            k = ord(nieuw_woord[i]) + n
            nieuw_woord += chr(k)
            if woord[i] == '@':
                nieuw_woord += ' '
    return nieuw_woord

def versleutel_zin(zin):
    spaties = ' '
    for woorden in zin:
        nieuwe_zin = ''
        if zin[woorden] == ' ':
            nieuwe_zin += versleutel_woord(woorden[::woorden])
    for spaties in zin:
        spaties = '@'

    return zin
