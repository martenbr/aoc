from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    counts = defaultdict(int)
    for line in aocutils.readlines(file):
        x0, y0, x1, y1 = [int(i) for i in aocutils.multisplit(line, [',', ' -> ', ','])]

        if x0 != x1 and y0 != y1:
            continue
        if x0 == x1:
            for i in range(min(y0, y1), max(y0, y1) + 1):
                counts[(x0, i)] += 1
        elif y0 == y1:
            for i in range(min(x0, x1), max(x0, x1) + 1):
                counts[(i, y0)] += 1
        else:
            assert False

    n = 0
    for x in counts.values():
        if x >= 2:
            n += 1
    print(n)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
