def versleutel(woord, n):
    versleuteld_woord = ''
    woord = woord.upper()
    for letter in woord:
        versleuteld_letter = chr(ord(letter) + n)
        if versleuteld_letter == '@':
            versleuteld_letter = ' '
        versleuteld_woord += versleuteld_letter

    return versleuteld_woord
def versleutel_zin(zin, getal):
    index_spatie = zin.fin(' ')
    code = ''

    while index_spatie != -1:
        woord = zin[:index_spatie]
        zin = zin[index_spatie +1:]
        code += '@' + versleutel(woord, getal)
        index_spatie = zin.find(' ')

    if len(zin) > 0:
        code += '@' + versleutel(zin, getal)

    return code