import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for line in aocutils.readlines(file):
        grid.append([int(x) for x in line])

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
