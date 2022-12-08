import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for line in aocutils.readlines(file):
        grid.append([int(x) for x in line])
    m = 0
    for x0 in range(len(grid)):
        for y0 in range(len(grid[0])):
            score = 1
            v0 = grid[x0][y0]
            s = 0
            for x in range(x0 + 1, len(grid)):
                s += 1
                if grid[x][y0] < v0:
                    pass
                else:
                    break
            score *= s

            s = 0
            for x in range(x0 - 1, -1, -1):
                s += 1
                if grid[x][y0] < v0:
                    pass
                else:
                    break
            score *= s

            s = 0
            for y in range(y0 + 1, len(grid)):
                s += 1
                if grid[x0][y] < v0:
                    pass
                else:
                    break
            score *= s

            s = 0
            for y in range(y0 - 1, -1, -1):
                s += 1
                if grid[x0][y] < v0:
                    pass
                else:
                    break
            score *= s
            m = max(m, score)
    print(m)
if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
