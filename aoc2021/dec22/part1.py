import aocutils


def main(file):
    print("RUNNING", file)
    grid = set()
    for line in aocutils.readlines(file):
        parts = aocutils.multisplit(line, [' x=', '..', ',y=', '..', ',z=', '..'])
        action = parts[0]
        x0, x1, y0, y1, z0, z1 = [int(a) for a in parts[1:]]
        assert x0 <= x1
        assert y0 <= y1
        assert z0 <= z1
        x0 = max(x0, -50)
        y0 = max(y0, -50)
        z0 = max(z0, -50)
        x1 = min(x1, 50)
        y1 = min(y1, 50)
        z1 = min(z1, 50)

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    if action == 'on':
                        grid.add((x, y, z))
                    else:
                        grid.discard((x, y, z))
    print(len(grid))


if __name__ == '__main__':
    main("example0.txt")
    print(39, "?")
    main("example_part1.txt")
    print(590784, "?")
    main("input.txt")
