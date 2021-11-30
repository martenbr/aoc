import aocutils


def main():
    entries = [int(x) for x in aocutils.readlines("input.txt")]
    data = set(entries)
    entries.sort()
    for i, a in enumerate(entries):
        for j, b in enumerate(entries):
            if i == j:
                continue

            c = 2020 - a - b
            if c <= 0:
                break
            if c in data:
                print(a, '+', b, '+', c, '=', a + b + c)
                print(a, '*', b, '*', c, '=', a * b * c)
                return


if __name__ == '__main__':
    main()
