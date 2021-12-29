def GCD(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    if a > 0:
        return a
    return b

def LCM(a, b):
    return a // GCD(a, b) * b
