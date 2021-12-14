from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    currentp = sections[0][0]
    subs = {}

    for line in sections[1]:
        a, b = line.split(' -> ')
        subs[a] = b


    print(currentp)
    nextp = []
    for step in range(10):
        print(step)
        for i in range(len(currentp)-1):
            l = currentp[i:i + 2]
            if l in subs:
                nextp.append(l[0])
                nextp.append(subs[l])
            else:
                nextp.append(l[0])
        nextp.append(l[1])
        currentp = ''.join(nextp)
        nextp = []
    counts = defaultdict(int)
    for c in currentp:
        counts[c] += 1
    print(counts)
    values = sorted([(v, k) for k, v in counts.items()])
    print(values)
    print(values[-1][0]-values[0][0])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
