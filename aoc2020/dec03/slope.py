def main():
    map = []
    for line in open("input.txt"):
        row = set()
        for i, char in enumerate(line):
            if char == '#':
                row.add(i)
        map.append(row)

    width = len(line)
    x = 0
    count = 0
    for row in map:
        if x % width in row:
            count += 1
        x += 3
    print(count)


if __name__ == '__main__':
    main()
