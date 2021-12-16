import heapq

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
    print(dijkstra(neighbors, start, dest))


def dijkstra(neighbors, start, dest):
    costs = {}
    q = [(0, start)]
    while q:
        cost, node = heapq.heappop(q)
        if node == dest:
            return cost
        for edge_cost, node in neighbors(node):
            new_cost = cost + edge_cost
            if node in costs and costs[node] <= new_cost:
                continue
            costs[node] = new_cost
            heapq.heappush(q, (new_cost, node))
    assert False


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
