def vec_rad(vx, vy):
    if vx == 0:
        rad = math.pi / 2
        if vy < 0:
            rad += math.pi
    else:
        rad = math.atan(vy/vx)
        if vx < 0:
            rad += math.pi
        if vx > 0 and vy < 0:
            rad += 2*math.pi
