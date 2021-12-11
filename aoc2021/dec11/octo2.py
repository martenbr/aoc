import aocutils


def neighbors(map, y, x):
    xs = [x]
    ys = [y]
    if x != 0:
        xs.append(x - 1)
    if x != len(map[0]) - 1:
        xs.append(x + 1)
    if y != 0:
        ys.append(y - 1)
    if y != len(map) - 1:
        ys.append(y + 1)
    for x1 in xs:
        for y1 in ys:
            if x1 == x and y1 == y:
                continue
            yield y1, x1


def main(file):
    print("RUNNING", file)
    map = []
    for line in aocutils.readlines(file):
        map.append([int(x) for x in line])
    flashes = 0
    all_of_them = len(map) * len(map[0])
    for step in range(1, 10_000):
        flashed = set()
        for y in range(len(map)):
            for x in range(len(map[0])):
                map[y][x] += 1

        prev_flashes = -1
        while flashes != prev_flashes:
            prev_flashes = flashes
            for y in range(len(map)):
                for x in range(len(map[0])):
                    if map[y][x] > 9 and (y, x) not in flashed:
                        flashed.add((y, x))
                        flashes += 1
                        for y1, x1 in neighbors(map, y, x):
                            map[y1][x1] += 1
        for y, x in flashed:
            map[y][x] = 0
        if len(flashed) == all_of_them:
            print(step)
            break


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
