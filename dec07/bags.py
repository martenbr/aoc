from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    lookup = defaultdict(set)
    for line in aocutils.readlines(file):
        line = line.strip()
        line = line.strip(".")
        bag, rest = line.split(" contain ")
        bag = bag[:-1]
        if rest != "no other bags":
            for x in rest.split(", "):
                c, name = x.split(" ", 1)
                c = int(c)
                if c != 1:
                    name = name[:-1]
                lookup[bag].add(name)
    find = "shiny gold bag"
    found = set()
    changed = True
    while changed:
        count = len(found)
        for bag in lookup.keys():
            contents = lookup[bag]
            if find in contents or any(c for c in contents if c in found):
                found.add(bag)
        changed = count != len(found)
    print(found)
    print(len(found))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
