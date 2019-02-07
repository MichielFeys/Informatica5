def geldige_zet(zet):
    mes = False
    # controleren of index 0 in k,l +++
    if len(zet) == 3 and zet[0] in 'KDTLP' and zet[1] in 'absdefg' and zet[2] in '12345678':
        mes = True
    elif len(zet) == 2 and zet[0] in 'absdefg' and zet[1] in '12345678':
        mes = True
    else:
        mes = False

    return mes

def geldige_zetten(zetten):
    i = 0
    while i < len(zetten) and geldige_zet(zetten[i]):
        i += 1

    return i >= len(zetten)