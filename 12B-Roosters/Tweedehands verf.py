def kleur_toevoegen(lijst, kleur):
    for i in range(0, len(lijst)):
        if kleur == 'rood':
            lijst[0] = lijst[0] + 1
        if kleur == 'groen':
            lijst[1] = lijst[1] + 1
        if kleur == 'blauw':
            lijst[2] = lijst[2] + 1
        return lijst

def is_wit(lijst):
    for i in range(0, len(lijst)):
        if lijst[0] == lijst[1] == lijst[2]:
            return True
        else:
            return False
def verf_verzamelen(lijst):
    begin_lijst = [0, 0, 0]
    aantal_gebruikt = 0
    for i in range(0, len(lijst)):

        while is_wit(kleur_toevoegen(begin_lijst, lijst[i])) is not True:
            aantal_gebruikt += 1

    return aantal_gebruikt, begin_lijst



print(verf_verzamelen(['rood', 'rood', 'blauw', 'blauw', 'rood', 'rood', 'rood', 'groen', 'blauw', 'groen', 'groen', 'groen', 'blauw', 'blauw', 'groen', 'blauw']))
print(kleur_toevoegen([0, 0, 0], 'groen'))