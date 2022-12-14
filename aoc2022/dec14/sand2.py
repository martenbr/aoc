import aocutils


def main(file):
    print("RUNNING", file)
    grid = set()
    xmin = 500
    xmax = 500
    ymax = 0
    for line in aocutils.readlines(file):
        prev = None
        for pair in line.split(' -> '):
            x, y = [int(x) for x in pair.split(',')]
            xmax = max(x, xmax)
            xmin = max(x, xmin)
            ymax = max(y, ymax)
            if prev:
                x0, y0 = prev
                if x == x0:
                    for i in range(min(y0, y), max(y0, y) + 1):
                        grid.add((x, i))
                elif y == y0:
                    for i in range(min(x0, x), max(x0, x) + 1):
                        grid.add((i, y))
                else:
                    assert False

            prev = (x, y)
    for x in range(xmin - 500, xmax + 500):
        grid.add((x, ymax + 2))
    before = len(grid)
    while True:
        x = 500
        y = 0
        while True:
            if (x, y + 1) not in grid:
                y = y + 1
            elif (x - 1, y + 1) not in grid:
                y = y + 1
                x = x - 1
            elif (x + 1, y + 1) not in grid:
                y = y + 1
                x = x + 1
            else:
                grid.add((x, y))
                if x == 500 and y == 0:
                    print(len(grid) - before)
                    return
                break


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
