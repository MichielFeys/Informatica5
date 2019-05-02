def vergeten_woorden(tekst, verplicht):
    woorden = set(tekst.split())
    #verplichte woorden
    aantal_verplicht = len(verplicht)
    #vergeten woorden
    vergeten = len(verplicht.difference(woorden))
    #gebruikte woorden
    gebruikte = len(woorden.intersection(verplicht))
    return aantal_verplicht, vergeten, gebruikte