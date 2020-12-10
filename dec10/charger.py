from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    lines = [int(l) for l in aocutils.readlines(file)]
    lines.sort()
    lines.append(lines[-1] + 3)
    diffs = defaultdict(lambda: 0)
    jole = 0
    for l in lines:
        diff = l - jole
        jole = l
        diffs[diff] += 1
    print(dict(diffs))
    print(diffs[1] * diffs[3])


if __name__ == '__main__':
    main("example.txt")
    main("example2.txt")
    main("input.txt")
