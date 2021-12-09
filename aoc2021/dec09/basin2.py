import aocutils


def neighbors(map, y, x):
    if x != 0:
        yield y, x - 1
    if x != len(map[0]) - 1:
        yield y, x + 1
    if y != 0:
        yield y - 1, x
    if y != len(map) - 1:
        yield y + 1, x


def is_low_point(map, y, x):
    for y1, x1 in neighbors(map, y, x):
        if map[y][x] >= map[y1][x1]:
            return False
    return True


def basin_size(map, y, x):
    contents = {(y, x)}
    to_check = [(y, x)]
    while to_check:
        for cord in neighbors(map, *to_check.pop()):
            y1, x1 = cord
            if map[y1][x1] != 9 and cord not in contents:
                contents.add(cord)
                to_check.append(cord)
    return len(contents)


def main(file):
    print("RUNNING", file)
    map = []
    for line in aocutils.readlines(file):
        map.append(([int(x) for x in line]))

    result = []
    for y, row in enumerate(map):
        for x, v in enumerate(row):
            if is_low_point(map, y, x):
                result.append(basin_size(map, y, x))
    result.sort(reverse=True)
    print(result[0] * result[1] * result[2])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
