def geldige_zet(zet):
    for i in range(0, len(zet)):
        if zet[i] in ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' and zet[i + 1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
        else:
            return True


def geldige_zetten(zetten):
    for i in range(0, len(zetten))