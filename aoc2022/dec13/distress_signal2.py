import functools

import aocutils


def compare(l1, l2):
    if isinstance(l1, list) and isinstance(l2, list):
        len1 = len(l1)
        len2 = len(l2)
        for i in range(min(len1, len2)):
            r = compare(l1[i], l2[i])
            if r != 0:
                return r
        return compare(len1, len2)
    elif isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        if l1 > l2:
            return 1
        return 0
    elif isinstance(l1, int):
        return compare([l1], l2)
    elif isinstance(l2, int):
        return compare(l1, [l2])
    else:
        assert False


def main(file):
    print("RUNNING", file)
    packets = []
    for i, sec in enumerate(aocutils.readsections(file)):
        l1 = eval(sec[0])
        l2 = eval(sec[1])
        packets.append(l1)
        packets.append(l2)
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compare))
    out = 1
    for i, p in enumerate(packets):
        if p == [[2]]:
            out *= i + 1
        elif p == [[6]]:
            out *= i + 1
    print(out)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
