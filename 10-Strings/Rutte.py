def tel_woorden_dov(zin):
    lengte = len(zin)
    lengte_zonder_spaties = len(zin.replace(' ',''))
    return lengte - lengte_zonder_spaties + 1


def tel_woorden(zin):

    aantal_spaties = 1

    for letter in zin:
        if letter ==' ':
            aantal_spaties += 1

    return aantal_spaties