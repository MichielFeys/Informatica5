def dronken_voeren(woord):
    nieuw_woord = woord[0]

    for i in range(1, len(woord)):
        if (i % 2) == 0 and i > 0:
            nieuw_woord += woord[i].upper()
        elif nieuw_woord[-1] in 'AEIOU':
            nieuw_woord += woord[i].upper()
        else:
            nieuw_woord += woord[i].lower()

    return nieuw_woord