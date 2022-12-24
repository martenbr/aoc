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

    for round in range(1, 9999):
        decisions = defaultdict(list)
        for e in elves:
            x, y = e
            if all((x + checkx, y + checky) not in elves for checkx, checky in around):
                continue
            for check, move in moves:
                if all((x + checkx, y + checky) not in elves for checkx, checky in check):
                    decisions[(x + move[0], y + move[1])].append(e)
                    break
        moved_elves = 0
        for dest, es in decisions.items():
            assert dest not in elves
            if len(es) == 1:
                moved_elves += 1
                elves.remove(es[0])
                elves.add(dest)

        if moved_elves == 0:
            break
        moves.append(moves.pop(0))

    print(round)


if __name__ == '__main__':
    #main("example0.txt")
    main("example.txt")
    main("input.txt")
