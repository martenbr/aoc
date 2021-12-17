import aocutils


def main(file):
    print("RUNNING", file)
    line = list(aocutils.readlines(file))[0]
    _, tx0, tx1, ty0, ty1 = aocutils.multisplit(line, ['target area: x=', '..', ', y=', '..'])
    tx0 = int(tx0)
    tx1 = int(tx1)
    ty0 = int(ty0)
    ty1 = int(ty1)
    maxy = None
    for y in range(1, 1000):
        ok, reached = simulate(0, y, tx0, tx1, ty0, ty1, ignore_x=True)
        if ok:
            maxy = y

    while maxy > 0:
        for x in range(1, tx1 + 1):
            ok, reached = simulate(x, maxy, tx0, tx1, ty0, ty1)
            if ok:
                print(x, maxy)
                print(reached)
                return
        maxy -= 1


def simulate(xdir, ydir, tx0, tx1, ty0, ty1, ignore_x=False):
    reached = 0
    x = 0
    y = 0
    while y >= ty0 and (ignore_x or x <= tx1):
        reached = max(reached, y)
        if y >= ty0 and y <= ty1 and (ignore_x or (x >= tx0 and x <= tx1)):
            return True, reached
        x += xdir
        y += ydir
        if xdir > 0:
            xdir -= 1
        elif xdir < 0:
            xdir += 1
        ydir -= 1

    return False, reached


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
