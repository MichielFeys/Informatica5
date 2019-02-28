def beweeg(coordinaat, richting):
    for i in range(0, len(coordinaat)):
        x_coordinaat = coordinaat[0]
        y_coordinaat = coordinaat[1]
        if richting == '<':
            x_coordinaat -= 1
        elif richting == '>':
            x_coordinaat += 1
        elif richting == '^':
            y_coordinaat += 1
        elif richting == 'v':
            y_coordinaat -= 1
        return x_coordinaat, y_coordinaat
def teruggekeerd(beweging):
    for i in range(0, len(beweging)):
        if beweging[0] == '<' and beweging[1] == '>' or beweging[0] == '>' and beweging[1] == '<':
            return True
        elif beweging[0] == 'v' and beweging[1] == '^' or beweging[0] == '^' and beweging[1] == 'v':
            return True
        else:
            return False

def laatste_levende_positie(bewegingen):
    for i in range(0, len(bewegingen)):
        x, y = beweeg((0, 0), bewegingen[i])
        i = 1
        while i < len(bewegingen) and not teruggekeerd([bewegingen[i-1], bewegingen[i]]):
            x, y = beweeg((x, y) , bewegingen[i])
            i += 1
        return i, x, y