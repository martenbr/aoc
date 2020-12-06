def main():
    group = []
    count = 0
    for line in open("input.txt"):
        line = line.strip()
        if line == "":
            s = None
            for p in group:
                if s is None:
                    s = p
                else:
                    s = s.intersection(p)
            count += len(s)
            print(len(s))
            group = []
            continue
        person = set(line)
        group.append(person)

    print(count)


if __name__ == '__main__':
    main()
