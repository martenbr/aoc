import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for line in aocutils.readlines(file):
        grid.append([int(x) for x in line])
    visible = set()
    for x in range(len(grid)):
        v = -1
        for y in range(len(grid[0])):
            if grid[x][y] > v:
                visible.add((x, y))
                v = grid[x][y]

        v = -1
        for y in reversed(range(len(grid[0]))):
            if grid[x][y] > v:
                visible.add((x, y))
                v = grid[x][y]
    for y in range(len(grid[0])):
        v = -1
        for x in range(len(grid)):
            if grid[x][y] > v:
                visible.add((x, y))
                v = grid[x][y]

        v = -1
        for x in reversed(range(len(grid))):
            if grid[x][y] > v:
                visible.add((x, y))
                v = grid[x][y]


    print(len(visible))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
