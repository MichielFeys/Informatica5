def volgend_collatz_getal(n):
    if n % 2 == 0:
         getal = n // 2
    else:
        getal = (n * 3) + 1

    return getal
def collatz():
