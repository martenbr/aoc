import aocutils


def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def main(file, checky):
    print("RUNNING", file)
    beacons = []
    minx = None
    maxx = None
    maxran = 0
    atchecky = set()
    for line in aocutils.readlines(file):
        x, y, bx, by = aocutils.parseints(line, negative=True)
        if by == checky:
            atchecky.add((bx, by))
        if minx is not None:
            minx = min(minx, x)
        else:
            minx = x
        if maxx is not None:
            maxx = max(maxx, x)
        else:
            maxx = x
        ran = dist(x, y, bx, by)
        beacons.append((x, y, ran))
        maxran = max(maxran, ran)
    y = checky
    cnt = 0
    for x in range(minx - maxran, maxx + maxran + 1):
        for bx, by, ran in beacons:
            if dist(x, y, bx, by) <= ran:
                cnt += 1
                break

    print(cnt-len(atchecky), cnt, '-', len(atchecky))


if __name__ == '__main__':
    main("example.txt", 10)
    main("input.txt", 2_000_000)
