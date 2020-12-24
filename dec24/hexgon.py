import aocutils


def main(file):
    print("RUNNING", file)
    flip_list = []
    for line in aocutils.readlines(file):
        i = 0
        instructions = []
        while i < len(line):
            c = line[i]
            if c == "n":
                i += 1
                c = line[i]
                if c == "e":
                    instructions.append("ne")
                elif c == "w":
                    instructions.append("nw")
            elif c == "s":
                i += 1
                c = line[i]
                if c == "e":
                    instructions.append("se")
                elif c == "w":
                    instructions.append("sw")
            elif c == "e":
                instructions.append("e")
            elif c == "w":
                instructions.append("w")
            i += 1
        flip_list.append(instructions)
    moves = dict(
        ne=(1, 1),
        se=(1, -1),
        e=(2, 0),
        nw=(-1, 1),
        sw=(-1, -1),
        w=(-2, 0),
    )
    black = set()
    for instructions in flip_list:
        x = 0
        y = 0
        for inst in instructions:
            dx, dy = moves[inst]
            x += dx
            y += dy
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.add((x, y))

    print("part1", len(black))

    def adjacent(cord):
        x, y = cord
        c = 0
        for dx, dy in moves.values():
            if (x + dx, y + dy) in black:
                c += 1
        return c

    for i in range(100):
        white = set()
        blacken = set()
        whiten = set()
        for x, y in black:
            for dx, dy in moves.values():
                white.add((x + dx, y + dy))
        for cord in black:
            b = adjacent(cord)
            if b == 0 or b > 2:
                whiten.add(cord)
        for cord in white:
            b = adjacent(cord)
            if b == 2:
                blacken.add(cord)
        black.update(blacken)
        black.difference_update(whiten)

    print("part2", len(black))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
