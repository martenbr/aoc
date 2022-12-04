import aocutils


def main(file):
    print("RUNNING", file)
    cnt = 0
    for line in aocutils.readlines(file):
        a, b, c, d = [int(x) for x in aocutils.multisplit(line, ['-', ',', '-'])]
        foo = set(range(a, b + 1))
        bar = set(range(c, d + 1))
        if foo.intersection(bar):
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
