import aocutils


def main(file):
    print("RUNNING", file)
    sum = 0
    for line in aocutils.readlines(file):
        b1 = set(line[:len(line) // 2])
        b2 = set(line[len(line) // 2:])
        item = next(iter(b1.intersection(b2)))
        if item.isupper():
            v = ord(item) - ord('A') + 27
        else:
            v = ord(item) - ord('a') + 1
        sum += v
    print(sum)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
