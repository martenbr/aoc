import aocutils


def main(file):
    print("RUNNING", file)
    active = set()
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    def print_map():
        for z in range(min_z, max_z + 1):
            print(f"z={z}")
            for y in range(min_y, max_y + 1):
                line = []
                for x in range(min_x, max_x + 1):
                    if (x, y, z) in active:
                        line.append('#')
                    else:
                        line.append('.')
                print(''.join(line))
            print()

    for y, line in enumerate(aocutils.readlines(file)):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0))
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    # print_map()

    for cycle in range(6):
        activate = []
        deactivate = []
        for z0 in range(min_z - 1, max_z + 2):
            for y0 in range(min_y - 1, max_y + 2):
                for x0 in range(min_x - 1, max_x + 2):
                    close = 0
                    for z in range(z0 - 1, z0 + 2):
                        for y in range(y0 - 1, y0 + 2):
                            for x in range(x0 - 1, x0 + 2):
                                if (x, y, z) in active:
                                    close += 1
                    if (x0, y0, z0) in active:
                        close -= 1
                        if close not in [2, 3]:
                            deactivate.append((x0, y0, z0))
                    else:
                        if close == 3:
                            activate.append((x0, y0, z0))
        for cord in deactivate:
            active.remove(cord)
        for cord in activate:
            active.add(cord)
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        min_z -= 1
        max_z += 1
        # print("cycle", cycle + 1)
        # print_map()
    print(len(active))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
