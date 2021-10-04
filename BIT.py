Bit = [0]*(N+10)

def add(pos, val):
    pos += 1
    while pos < len(Bit):
        Bit[pos] += val
        pos += pos & -pos

def get(pos):
    ret = 0
    pos += 1
    while pos > 0:
        ret += Bit[pos]
        pos -= pos & -pos
    return ret
