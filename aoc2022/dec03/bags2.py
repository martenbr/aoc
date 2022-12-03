import aocutils


def main(file):
    print("RUNNING", file)
    sum = 0
    i = 0
    groups = []
    group = []
    for line in aocutils.readlines(file):
        group.append(line)
        i += 1
        if i == 3:
            groups.append(group)
            group = []
            i = 0
    for g in groups:
        item = set(g[0]).intersection(g[1]).intersection(g[2])
        print(item)
        item = next(iter(item))
        if item.isupper():
            v = ord(item) - ord('A') + 27
        else:
            v = ord(item) - ord('a') + 1
        sum += v
    print(sum)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
