def hint(gok, woord):
    antw = ''
    for i in range(0, len(woord)):
        if gok[i] in woord:
            if gok[i] == woord[i]:
                antw += gok[i].upper()
            else:
                antw += gok[i]
        else:
            antw += '.'

    return antw