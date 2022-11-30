import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for line in aocutils.readlines(file):
        grid.append([int(x) for x in line])
    new_grid = []
    for line in grid:
        for i in range(5):
            new_grid.append([None for _ in range(len(line) * 5)])
    for y, line in enumerate(grid):
        for x, cost in enumerate(line):
            for i in range(5):
                for j in range(5):
                    new_cost = grid[y][x] + i + j
                    if new_cost > 9:
                        new_cost -= 9
                    new_grid[i * len(grid) + y][j * len(grid[0]) + x] = new_cost

    grid = new_grid

    def neighbors(node):
        x0, y0 = node
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = x0 + dx
            y = y0 + dy
            if x >= len(grid[0]) or x < 0:
                continue
            if y >= len(grid) or y < 0:
                continue
            edge_cost = grid[y][x]
            yield edge_cost, (x, y)

    start = (0, 0)
    dest = (len(grid[0]) - 1, len(grid) - 1)
    print(aocutils.dijkstra(neighbors, start, dest))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
