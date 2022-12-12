import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for y, line in enumerate(aocutils.readlines(file)):
        row = []
        for x, c in enumerate(line):
            if c == 'S':
                row.append(0)
            elif c == 'E':
                row.append(ord('z') - ord('a'))
                end = (y, x)
            else:
                row.append(ord(c) - ord('a'))
        grid.append(row)

    def neighbors(n):
        y, x = n
        if y + 1 < len(grid) and grid[y + 1][x] <= grid[y][x] + 1:
            yield 1, (y + 1, x)
        if y > 0 and grid[y - 1][x] <= grid[y][x] + 1:
            yield 1, (y - 1, x)
        if x + 1 < len(grid[0]) and grid[y][x + 1] <= grid[y][x] + 1:
            yield 1, (y, x + 1)
        if x > 0 and grid[y][x - 1] <= grid[y][x] + 1:
            yield 1, (y, x - 1)

    cost = 99999
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                start = (y, x)
                try:
                    c = aocutils.dijkstra(neighbors, start, end)
                    cost = min(cost, c)
                except AssertionError:
                    pass
    print(cost)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
