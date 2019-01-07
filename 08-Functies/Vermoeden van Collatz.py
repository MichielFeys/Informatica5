def volgend_collatz_getal(n):
    if n % 2 == 0:
         getal = n // 2
    else:
        getal = (n * 3) + 1

    return getal



def collatz(n):
    lengte = 0
    if n == 1:
        lengte += 1
    else:
        lengte += 1 + collatz(volgend_collatz_getal(n))

    return lengte