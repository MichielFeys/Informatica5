def ontdubbelen(woord):
    nieuw_woord = ''
    for i in range(0, len(woord)):
        if woord[i] == woord[i-1] and woord[i] != woord[0]:
            nieuw_woord += woord[::i-2] + woord[i] + woord[i + 1::]
        elif woord[i] == woord[i+1]:
            nieuw_woord += woord[0:i-1] + woord[i] + woord[i+1::]
        elif woord[i] == woord[i-1] and woord[i] == woord[i+1]:
            nieuw_woord += woord[::i-2] + woord[i] + woord[i+2::]
        else:
            nieuw_woord = woord
    return nieuw_woord

