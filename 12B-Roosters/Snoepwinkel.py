from operator import itemgetter
def bereken_prijs(lijst):
    antw = 0
    for item in lijst:
        antw += item[1]

    return antw
def winkelbriefje(lijst):
    antw = []
    for i in range(len(lijst)):
        antw.append(lijst[i][0])
    return antw

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst