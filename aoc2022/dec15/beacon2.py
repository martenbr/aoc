import aocutils


def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def main(file, maxcord):
    print("RUNNING", file)
    scanners = []

    for line in aocutils.readlines(file):
        x, y, bx, by = aocutils.parseints(line, negative=True)
        ran = dist(x, y, bx, by)
        scanners.append((x, y, ran))
    for dir in (True, False):
        for scanx, scany, ran in scanners:
            skirtrange = ran + 1
            minx = max(0, scanx - skirtrange)
            maxx = min(maxcord, scanx + skirtrange)
            bx = minx
            while bx <= maxx:
                if dir:
                    by = scany - (skirtrange - abs(scanx - bx))
                else:
                    by = scany + (skirtrange - abs(scanx - bx))
                if (by < 0 or by > maxcord) and bx < scanx:
                    bx = scanx + (scanx-bx)
                    continue
                slacks = []
                for sx2, sy2, ran2 in scanners:
                    slack = ran2 - dist(sx2, sy2, bx, by)
                    slacks.append(slack)
                maxslack = max(slacks)
                if maxslack < 0:
                    if by > 0 and by <= maxcord:
                        print(bx * 4000000 + by)
                        return

                bx += max(maxslack // 2, 1)


if __name__ == '__main__':
    main("example.txt", 20)
    main("input.txt", 4_000_000)
