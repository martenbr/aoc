import aocutils


def main():
    entries = [int(x) for x in aocutils.readlines("input.txt")]
    data = set(entries)
    for a in entries:
        b = 2020 - a
        if b in data:
            print(a, '+', b, '=', a + b)
            print(a, '*', b, '=', a * b)


if __name__ == '__main__':
    main()
