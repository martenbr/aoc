def main():
    map = []
    for line in open("input.txt"):
        row = set()
        for i, char in enumerate(line):
            if char == '#':
                row.add(i)
        map.append(row)

    width = len(line)
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    tot = 1
    for deltax, deltay in slopes:
        x = 0
        count = 0
        for y, row in enumerate(map):
            if deltay != 1 and y % deltay != 0:
                continue
            if x % width in row:
                count += 1
            x += deltax
        tot *= count
        print(count)
    print(tot)


if __name__ == '__main__':
    main()
