from collections import defaultdict

import aocutils


def printmap(elves, minx=None, maxx=None, miny=None, maxy=None):
    if not minx:
        minx = min(x for x, _ in elves)
    if not maxx:
        maxx = max(x for x, _ in elves)
    if not miny:
        miny = min(y for _, y in elves)
    if not maxy:
        maxy = max(y for _, y in elves)
    for y in range(miny, maxy + 1):
        l = []
        for x in range(minx, maxx + 1):
            if (x, y) in elves:
                l.append('#')
            else:
                l.append('.')
        print(''.join(l))
    print()


def main(file):
    print("RUNNING", file)
    elves = set()
    for y, line in enumerate(aocutils.readlines(file)):
        for x, char in enumerate(line):
            if char == '#':
                elves.add((x, y))

    moves = [
        ([(0, -1), (-1, -1), (1, -1)], (0, -1)),
        ([(0, 1), (-1, 1), (1, 1)], (0, 1)),
        ([(-1, 0), (-1, -1), (-1, 1)], (-1, 0)),
        ([(1, 0), (1, -1), (1, 1)], (1, 0)),
    ]
    around = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for _ in range(10):
        decisions = defaultdict(list)
        for e in elves:
            x, y = e
            if all((x + checkx, y + checky) not in elves for checkx, checky in around):
                continue
            for check, move in moves:
                if all((x + checkx, y + checky) not in elves for checkx, checky in check):
                    decisions[(x + move[0], y + move[1])].append(e)
                    break
        for dest, es in decisions.items():
            assert dest not in elves
            if len(es) == 1:
                elves.remove(es[0])
                elves.add(dest)
        #printmap(elves, -3, 10, -2, 9)
        moves.append(moves.pop(0))
    minx = min(x for x, _ in elves)
    maxx = max(x for x, _ in elves)
    miny = min(y for _, y in elves)
    maxy = max(y for _, y in elves)
    print((maxx + 1 - minx) * (maxy + 1 - miny) - len(elves))


if __name__ == '__main__':
    main("example0.txt")
    main("example.txt")
    main("input.txt")
