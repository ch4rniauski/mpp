def gcd_iter(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_rec(b, a % b)
