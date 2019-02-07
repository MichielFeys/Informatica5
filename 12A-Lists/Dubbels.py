def dubbels(x):
    y = []
    for i in x:
        if x.count(i) > 1 and i not in y:
            y.append(i)

    return y