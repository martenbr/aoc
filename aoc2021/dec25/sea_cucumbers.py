import aocutils


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    map = {}
    maxy = len(lines)
    maxx = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != '.':
                map[(x, y)] = c
    for step in range(1, 99999):
        new_map = step_once(map, maxx, maxy)
        if map == new_map:
            break
        map = new_map
    print(step)


def step_once(map, maxx, maxy):
    new_map = dict()
    for cord, c in map.items():
        if c == '>':
            x, y = cord
            new_x = x + 1
            if new_x == maxx:
                new_x = 0
            if (new_x, y) not in map:
                new_map[(new_x, y)] = c
                continue
        new_map[cord] = c
    map = new_map
    new_map = dict()
    for cord, c in map.items():
        if c == 'v':
            x, y = cord
            new_y = y + 1
            if new_y == maxy:
                new_y = 0
            if (x, new_y) not in map:
                new_map[(x, new_y)] = c
                continue
        new_map[cord] = c
    return new_map


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
