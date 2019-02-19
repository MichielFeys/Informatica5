def printbaar_rek(lijst):
    rij_een = lijst[-1][0] + lijst[-1][1] + lijst[-1][2] + lijst[-1][3] +lijst[-1][4]
    rij_twee = lijst[-2][0] + lijst[-2][1] + lijst[-2][2] + lijst[-2][3] +lijst[-2][4]
    rij_drie = lijst[-3][0] + lijst[-3][1] + lijst[-3][2] + lijst[-3][3] +lijst[-3][4]
    rij_vier = lijst[-4][0] + lijst[-4][1] + lijst[-4][2] + lijst[-4][3] +lijst[-4][4]

    return rij_een + '\n' + rij_twee + '\n' + rij_drie + '\n' + rij_vier

def speel(kleur, kolom, lijst):
    for i in range(len(lijst)):
        if lijst[i][kolom] == 'O':
            lijst[0][kolom] = kleur
        elif lijst[0][kolom] != 'O' and lijst[1][kolom] == 'O':
            lijst[1][kolom] = kleur
        elif lijst[0][kolom] != 'O' and lijst[1][kolom]!= 'O' and lijst[2][kolom] == 'O':
            lijst[2][kolom] = kleur
        elif lijst[0][kolom] != 'O' and lijst[1][kolom]!= 'O' and lijst[2][kolom] != 'O' and lijst[3][kolom] == 'O':
            lijst[3][kolom] = kleur
        return lijst