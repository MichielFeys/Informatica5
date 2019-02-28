def ontdubbelen(woord):
    nieuw_woord =''
    for i in range(0, len(woord)):
        if woord.count(i) > 1:
            nieuw_woord += woord.remove(i) + i

        else:
            nieuw_woord = woord

        return nieuw_woord