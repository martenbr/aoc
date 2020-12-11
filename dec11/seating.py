import aocutils


def find_changed(map):
    width = len(map[0])
    height = len(map)

    def adjacent(c1, c2):
        count = 0
        for i in range(c1 - 1, c1 + 2):
            if i < 0 or i >= height:
                continue
            for j in range(c2 - 1, c2 + 2):
                if j < 0 or j >= width:
                    continue
                if i == c1 and j == c2:
                    continue
                val = map[i][j]
                if val:
                    count += 1
        return count

    for a, row in enumerate(map):
        for b in range(width):
            current = map[a][b]
            if current is None:
                continue
            occupied = adjacent(a, b)
            if current is False:
                if occupied == 0:
                    yield a, b, True
            if current is True:
                if occupied >= 4:
                    yield a, b, False


def print_map(map):
    for row in map:
        line = []
        for x in row:
            if x is None:
                line.append('.')
            elif x is False:
                line.append('L')
            elif x is True:
                line.append('#')
        print(''.join(line))
    print()


def main(file):
    print("RUNNING", file)
    map = []
    for line in aocutils.readlines(file):
        row = []
        for c in line:
            if c == 'L':
                row.append(True)
            else:
                row.append(None)
        map.append(row)
    # print_map(map)
    while True:
        changed = list(find_changed(map))
        if not changed:
            break
        for a, b, val in changed:
            map[a][b] = val
        # print_map(map)
    count = 0
    for row in map:
        for v in row:
            if v:
                count += 1

    print(count)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
