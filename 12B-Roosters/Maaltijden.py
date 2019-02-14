def maaltijdsprijs(maaltijdtype, aantal):
    maaltijdprijs = 0
    if maaltijdtype == 'middagmaal':
        maaltijdprijs = aantal * 5.3
    elif maaltijdtype == 'soep':
        maaltijdprijs = aantal * 1.7
    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs = aantal * 2.3
    return maaltijdprijs


def dagprijs(bestelling):
    som = 0
    for i in range(0, len(bestelling), 2):
        som += maaltijdsprijs(bestelling[i], bestelling[i+1])
    return som

def weekprijs(bestelling):
    weekprijs = 0
    for dag in bestelling:
        weekprijs += dagprijs(dag)
    return weekprijs