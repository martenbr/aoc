import aocutils


def main(file):
    print("RUNNING", file)
    lookup = {}
    for line in aocutils.readlines(file):
        line = line.strip()
        line = line.strip(".")
        bag, rest = line.split(" contain ")
        bag = bag[:-1]
        contents = []
        if rest != "no other bags":
            for x in rest.split(", "):
                c, name = x.split(" ", 1)
                c = int(c)
                if c != 1:
                    name = name[:-1]
                contents.append((c, name))
        lookup[bag] = contents
    find = "shiny gold bag"
    counts = {}
    changed = True
    while changed:
        known = len(counts)
        for bag, contents in lookup.items():
            count = 1
            ok = True
            for c, b in contents:
                if b not in counts:
                    ok = False
                    break
                count += c * counts[b]
            if ok:
                counts[bag] = count

        changed = known != len(counts)
    print(counts)
    print(counts[find] - 1)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
