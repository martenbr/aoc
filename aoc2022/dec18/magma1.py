import aocutils


def main(file):
    print("RUNNING", file)
    grid = set()
    for line in aocutils.readlines(file):
        c = tuple(aocutils.parseints(line))
        grid.add(c)

    cnt = 0
    for x, y, z in grid:
        if (x + 1, y, z) not in grid:
            cnt += 1
        if (x - 1, y, z) not in grid:
            cnt += 1
        if (x, y + 1, z) not in grid:
            cnt += 1
        if (x, y - 1, z) not in grid:
            cnt += 1
        if (x, y, z + 1) not in grid:
            cnt += 1
        if (x, y, z - 1) not in grid:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
