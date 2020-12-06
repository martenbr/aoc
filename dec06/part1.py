def main():
    group = set()
    count = 0
    for line in open("input.txt"):
        line = line.strip()
        if line == "":
            count += len(group)
            print(len(group))
            group = set()
            continue
        for c in line:
            group.add(c)

    print(count)


if __name__ == '__main__':
    main()
