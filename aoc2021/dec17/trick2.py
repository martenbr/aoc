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
        if simulate(0, y, tx0, tx1, ty0, ty1, ignore_x=True):
            maxy = y

    success = set()
    while maxy > -1000:
        for x in range(1, tx1 + 1):
            if simulate(x, maxy, tx0, tx1, ty0, ty1):
                success.add((x, maxy))
        maxy -= 1
    print(len(success))


def simulate(xdir, ydir, tx0, tx1, ty0, ty1, ignore_x=False):
    reached = 0
    x = 0
    y = 0
    while y >= ty0 and (ignore_x or x <= tx1):
        reached = max(reached, y)
        if y >= ty0 and y <= ty1 and (ignore_x or (x >= tx0 and x <= tx1)):
            return True
        x += xdir
        y += ydir
        if xdir > 0:
            xdir -= 1
        elif xdir < 0:
            xdir += 1
        ydir -= 1

    return False


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
