def volgende_rij(lijst):
    volgende = []
    for i in lijst:
        if lijst.count(i) == len(lijst):
            volgende += (len(lijst) - 1) *[i]
        elif i == 'G' and i + 1 == 'R':
            volgende += ['Y']
        return volgende