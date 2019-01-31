from math import sqrt
def binnen_of_buiten(m, c, p):
    antw = ''
    #straal = afst m tot c
    r = sqrt( pow(m[0] - c[0], 2) + pow(m[1] - c[1], 2))
    # afst d: van m tot p
    d = sqrt( pow(m[0] - p[0], 2) + pow(m[1] - p[1], 2))
    if r == d:
        antw += 'op'
    elif r < d:
        antw += 'buiten'
    elif r > d:
        antw += 'binnen'

    return (antw, d)