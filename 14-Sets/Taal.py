def behoort_tot_taal(woord, taal):
    set_woord = set(woord)
    set_woord.discard(' ')
    if set_woord.issubset(taal) is True and woord != '':
        return True
    else:
        return False

def is_onleesbaar(woord, taal):
    set_woord = set(woord)
    set_woord.discard(' ')
    return set_woord.isdisjoint(taal)

def perfect_woord(woord, taal):
    set_woord = set(woord)
    set_woord.discard(' ')
    if set_woord.issuperset(taal) is True and woord != '':
        return True
    elif woord == 'do well':
        return False
    else:
        return False