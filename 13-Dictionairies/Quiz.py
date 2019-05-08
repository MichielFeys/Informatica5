def verlaat_ploeg(verlater, ploeg, lijst):
    team = lijst[ploeg]
    team.remove(verlater)
    lijst[ploeg] = team
    if lijst[ploeg] == []:
        lijst.pop(ploeg)
    return lijst

def vervoegt_ploeg(vervoeger, ploeg, lijst):
    if ploeg in lijst:
        team = lijst[ploeg]
        team.append(vervoeger)
        lijst[ploeg] = team
    else:
        lijst[ploeg] = [vervoeger]
    return lijst
