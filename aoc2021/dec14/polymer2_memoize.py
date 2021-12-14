from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    poly = sections[0][0]
    subs = {}

    for line in sections[1]:
        a, b = line.split(' -> ')
        subs[a] = b

    cache = dict()

    def expand_and_count(pair, num_expands):
        if num_expands == 0:
            result = defaultdict(int)
            result[pair[0]] += 1
            result[pair[1]] += 1
            return result
        elif (pair, num_expands) in cache:
            return cache[(pair, num_expands)]
        else:
            new_char = subs[pair]
            r1 = expand_and_count(pair[0] + new_char, num_expands - 1)
            r2 = expand_and_count(new_char + pair[1], num_expands - 1)
            result = r1.copy()
            for k, v in r2.items():
                result[k] += v
            result[new_char] -= 1
            cache[(pair, num_expands)] = result
            return result

    total_counts = defaultdict(int)
    for i in range(len(poly) - 1):
        for k, v in expand_and_count(poly[i:i + 2], 40).items():
            total_counts[k] += v
    for i in range(1, len(poly) - 1):
        total_counts[poly[i]] -= 1
    values = sorted([(v, k) for k, v in total_counts.items()])
    print(len(cache))
    print(values)
    print(values[-1][0] - values[0][0])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
