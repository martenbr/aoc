import aocutils


def main(file):
    print("RUNNING", file)
    magma = []
    for line in aocutils.readlines(file):
        c = tuple(aocutils.parseints(line))
        magma.append(c)

    cnt = 0
    minx = min(c[0] for c in magma)
    maxx = max(c[0] for c in magma)
    miny = min(c[1] for c in magma)
    maxy = max(c[1] for c in magma)
    minz = min(c[2] for c in magma)
    maxz = max(c[2] for c in magma)

    nonwater = set(magma)

    def neighbors(n):
        x, y, z = n
        yield x + 1, y, z
        yield x - 1, y, z
        yield x, y + 1, z
        yield x, y - 1, z
        yield x, y, z + 1
        yield x, y, z - 1

    searched = set()
    for x in range(minx + 1, maxx):
        for y in range(miny + 1, maxy):
            for z in range(minz + 1, maxz):
                start = (x, y, z)
                if start in nonwater:
                    continue
                if start in searched:
                    continue
                space = set()
                space.add(start)
                iswater = False
                q = [start]
                while q:
                    foo = q.pop()
                    for c in neighbors(foo):
                        if c in nonwater:
                            continue
                        if c in space:
                            continue

                        searched.add(c)
                        space.add(c)
                        if c[0] == minx or c[0] == maxx or c[1] == miny or c[1] == maxy or c[2] == minz or c[2] == maxz:
                            iswater = True
                            continue
                        q.append(c)
                if not iswater:
                    # air gap
                    for c in space:
                        nonwater.add(c)

    for c in magma:
        for n in neighbors(c):
            if n not in nonwater:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
