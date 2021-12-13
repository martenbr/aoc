from itertools import zip_longest

import aocutils


def hflip(data):
    # Flip across the horizontal axis (swapping top and bot)
    return list(reversed(data))


def vflip(data):
    # Flip across the vertical axis (swapping left and right)
    return [list(reversed(d)) for d in data]


def merge(p1, p2):
    result = []
    for r1, r2 in zip_longest(p1, p2, fillvalue=[]):
        result.append([(a or b) for (a, b) in zip_longest(r1, r2, fillvalue=False)])
    return result


def print_grid(g):
    for line in g:
        print(''.join(('#' if c else '.') for c in line))
    print()


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    maxx = 0
    maxy = 0
    for line in sections[0]:
        x, y = [int(a) for a in line.split(',')]
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    grid = []
    for _ in range(maxy + 1):
        grid.append([False for _ in range(maxx + 1)])
    for line in sections[0]:
        x, y = [int(x) for x in line.split(',')]
        grid[y][x] = True

    folds = sections[1]

    for fold in folds:
        instr, v = fold.split('=')
        v = int(v)
        if instr == "fold along x":
            part1 = [r[:v] for r in grid]
            part2 = [r[v + 1:] for r in grid]
            part1 = vflip(part1)
            result = merge(part1, part2)
            result = vflip(result)
            grid = result
        elif instr == "fold along y":
            part1 = grid[:v]
            part2 = grid[v + 1:]
            part1 = hflip(part1)
            result = merge(part1, part2)
            result = hflip(result)
            grid = result

    print_grid(grid)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
