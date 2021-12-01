import aocutils


def main(file):
    print("RUNNING", file)
    cnt = 0
    prev = None
    for a in window_sums(file):
        if prev is not None:
            if a > prev:
                cnt += 1
        prev = a
    print(cnt)


def window_sums(file):
    b = None
    c = None
    for line in aocutils.readlines(file):
        a = int(line)
        if b is not None and c is not None:
            yield a + b + c
        b, c = a, b


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
