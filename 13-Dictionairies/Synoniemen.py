def synoniemen(zin, synoniemen):
    #zin in lijst zetten
    zin = zin.split()
    #zoek woord op in synoniemen
    for i in range(0, len(zin)):
        if zin[i] in synoniemen:
            zin[i] = synoniemen.get(zin[i])
    #lijst terug samen
    zin = ' '.join(zin)
    return zin







