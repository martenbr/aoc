import aocutils


def main(file):
    print("RUNNING", file)
    grid = []
    for line in aocutils.readlines(file):
        grid.append([int(x) for x in line])
    costs = {}
    costs[(0, 0)] = 0
    q = [(0, 0, 0)]
    while q:
        cost, x, y = q.pop()
        #print(x,y,cost)
        if x == len(grid[0])-1 and y == len(grid)-1:
            print(cost)
            return
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x1 = x + dx
            y1 = y + dy
            if x1 >= len(grid[0]) or x1 < 0:
                continue
            if y1 >= len(grid) or y1 < 0:
                continue
            new_cost = cost + grid[y1][x1]
            if (x1, y1) in costs and costs[(x1, y1)] <= new_cost:
                continue
            costs[(x1, y1)] = new_cost
            q.append((new_cost, x1, y1))
        q.sort(reverse=True)
    assert False


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
