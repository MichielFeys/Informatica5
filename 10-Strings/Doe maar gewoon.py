def doe_maar_gewoon(woord):
    nieuw_woord = ''

    for i in range(1, len(woord)-1):
        if woord[i].lower() == woord[i+1].lower() and woord[i] == woord[i].upper():
            nieuw_woord += woord[0:i-1] + woord[i].lower() + woord[i::]

    return nieuw_woord


