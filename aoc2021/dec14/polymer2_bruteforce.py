from collections import defaultdict

import aocutils


def expand20x(poly, subs):
    currentp = poly
    nextp = []
    for step in range(20):
        for i in range(len(currentp) - 1):
            l = currentp[i:i + 2]
            if l in subs:
                nextp.append(l[0])
                nextp.append(subs[l])
            else:
                nextp.append(l[0])
        nextp.append(l[1])
        currentp = ''.join(nextp)
        nextp = []
    return currentp


def count_chars(poly):
    counts = defaultdict(int)
    for c in poly:
        counts[c] += 1
    counts[poly[-1]] -= 1
    return dict(counts)


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    currentp = sections[0][0]
    subs = {}
    subs20 = {}

    for line in sections[1]:
        a, b = line.split(' -> ')
        subs[a] = b

    # Pre calculate result of doing 20 expansion for all pairs
    for a in subs.keys():
        print(a)
        subs20[a] = expand20x(a, subs)

    # Expand x20
    nextp = []
    for i in range(len(currentp)-1):
        pair = currentp[i:i + 2]
        nextp.append(subs20[pair][:-1])

    nextp.append(pair[1])
    currentp = ''.join(nextp)

    # Expand x20 again, but only count characters this time
    counts20 = {}
    total_count = defaultdict(int)
    for i in range(len(currentp) - 1):
        pair = currentp[i:i + 2]
        if pair not in counts20:
            counts20[pair] = count_chars(subs20[pair])

        for k, v in counts20[pair].items():
            total_count[k] += v
    total_count[pair[-1]] += 1

    values = sorted([(v, k) for k, v in total_count.items()])
    print(values)
    print(values[-1][0]-values[0][0])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
