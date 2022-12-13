import aocutils


def compare(l1, l2):
    if isinstance(l1, list) and isinstance(l2, list):
        len1 = len(l1)
        len2 = len(l2)
        for i in range(min(len1, len2)):
            r = compare(l1[i], l2[i])
            if r is not None:
                return r
        return compare(len1, len2)
    elif isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return True
        if l1 > l2:
            return False
        return None
    elif isinstance(l1, int):
        return compare([l1], l2)
    elif isinstance(l2, int):
        return compare(l1, [l2])
    else:
        assert False


def main(file):
    sum = 0
    print("RUNNING", file)
    for i, sec in enumerate(aocutils.readsections(file)):
        l1 = eval(sec[0])
        l2 = eval(sec[1])
        if compare(l1, l2) is True:
            sum += i + 1
    print(sum)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
