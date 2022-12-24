import functools
import heapq
from collections import defaultdict

import aocutils


def astar(neighbors, estimate_remaining, start, is_goal):
    costs = {}
    q = [(estimate_remaining(start), 0, start)]
    while q:
        _, cost, cnode = heapq.heappop(q)
        if is_goal(cnode):
            return cost
        for edge_cost, node in neighbors(cnode):
            new_cost = cost + edge_cost
            if node in costs and costs[node] <= new_cost:
                continue
            costs[node] = new_cost
            heapq.heappush(q, (new_cost + estimate_remaining(node), new_cost, node))
    return costs


def main(file):
    print("RUNNING", file)
    wall_grid = []
    initial_blizzards = defaultdict(list)
    for y, line in enumerate(aocutils.readlines(file)):
        wall_row = []
        for x, c in enumerate(line):
            if c == '#':
                wall_row.append(c)
            else:
                wall_row.append('.')
            if c in ('<', '>', 'v', '^'):
                initial_blizzards[(x, y)].append(c)

        wall_grid.append(wall_row)

    @functools.lru_cache(None)
    def get_blizzards(t):
        if t == 0:
            return initial_blizzards
        else:
            prev = get_blizzards(t - 1)
        new_blizzards = defaultdict(list)
        for (x, y), arrows in prev.items():
            for arrow in arrows:
                if arrow == '<':
                    newx = x - 1
                    newy = y
                    if wall_grid[newy][newx] == '#':
                        newx = len(wall_grid[0]) - 2
                elif arrow == '>':
                    newx = x + 1
                    newy = y
                    if wall_grid[newy][newx] == '#':
                        newx = 1
                elif arrow == '^':
                    newx = x
                    newy = y - 1
                    if wall_grid[newy][newx] == '#':
                        newy = len(wall_grid) - 2
                elif arrow == 'v':
                    newx = x
                    newy = y + 1
                    if wall_grid[newy][newx] == '#':
                        newy = 1
                else:
                    assert False
                new_blizzards[(newx, newy)].append(arrow)
        return new_blizzards

    steps_to_goal = len(wall_grid) + len(wall_grid[0]) - 4

    def min_remaining(state):
        x, y, _, elves_delivered, snacks_fetched = state
        if snacks_fetched:
            return steps_to_goal - x - y + 1
        elif elves_delivered:
            return steps_to_goal + x + y - 1
        else:
            return steps_to_goal * 3 - x - y + 1

    goalx = len(wall_grid[0]) - 2
    goaly = len(wall_grid) - 1
    assert wall_grid[goaly][goalx] == '.'

    assert min_remaining((1, 0, None, False, False)) == steps_to_goal * 3
    assert min_remaining((1, 1, None, False, False)) == steps_to_goal * 3 - 1
    assert min_remaining((2, 1, None, False, False)) == steps_to_goal * 3 - 2
    assert min_remaining((1, 0, None, True, False)) == steps_to_goal
    assert min_remaining((1, 1, None, True, False)) == steps_to_goal + 1
    assert min_remaining((1, 0, None, True, True)) == steps_to_goal
    assert min_remaining((1, 1, None, True, True)) == steps_to_goal - 1
    assert min_remaining((goalx, goaly, None, True, True)) == 0

    def actions(state):
        x, y, t, elves_delivered, snacks_fetched = state
        blizzards = get_blizzards(t + 1)
        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            newx = x + dx
            newy = y + dy
            if newy < 0 or newy >= len(wall_grid):
                continue
            if wall_grid[newy][newx] == '#':
                continue
            if (newx, newy) not in blizzards:
                new_elves_delivered = elves_delivered or (newx == goalx and newy == goaly)
                new_snacks_fetched = snacks_fetched or (elves_delivered and newx == 1 and newy == 0)
                yield 1, (newx, newy, t + 1, new_elves_delivered, new_snacks_fetched)

    def is_goal(state):
        x, y, t, elves_delivered, snacks_fetched = state
        return elves_delivered and snacks_fetched and x == goalx and y == goaly

    assert is_goal((goalx, goaly, None, True, True))
    assert not is_goal((goalx, goaly, None, True, False))
    start = (1, 0, 0, False, False)
    t = astar(actions, min_remaining, start, is_goal)
    print(t)


if __name__ == '__main__':
    main("example0.txt")
    main("example.txt")
    main("input.txt")
