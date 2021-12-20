import aocutils


def main(file, rounds):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    algo = ''.join(sections[0])
    image = set()
    image_inverted = False
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for y, line in enumerate(sections[1]):
        for x, char in enumerate(line):
            if char == '#':
                image.add((x, y))
                maxy = max(maxy, y)
                maxx = max(maxx, x)
    invert_mode = False
    if algo[0] == '#':
        assert algo[0b111_111_111] == '.'
        invert_mode = True
    for round in range(rounds):
        new_image = set()
        new_image_inverted = invert_mode and not image_inverted
        outputx = list(range(minx - 1, maxx + 2))
        outputy = list(range(miny - 1, maxy + 2))
        for y in outputy:
            for x in outputx:
                bitstr = []
                for yi in range(y - 1, y + 2):
                    for xi in range(x - 1, x + 2):
                        if (xi, yi) in image:
                            if image_inverted:
                                bitstr.append('0')
                            else:
                                bitstr.append('1')
                        else:
                            if image_inverted:
                                bitstr.append('1')
                            else:
                                bitstr.append('0')
                val = int(''.join(bitstr), 2)

                if new_image_inverted:
                    is_filled = algo[val] == '.'
                else:
                    is_filled = algo[val] == '#'
                if is_filled:
                    new_image.add((x, y))
                    minx = min(minx, x)
                    miny = min(miny, y)

                    maxx = max(maxx, x)
                    maxy = max(maxy, y)
        image = new_image
        image_inverted = new_image_inverted

    print(len(image))


def print_image(image):
    minx = min(c[0] for c in image)
    maxx = max(c[0] for c in image)
    miny = min(c[1] for c in image)
    maxy = max(c[1] for c in image)
    for y in range(miny - 1, maxy + 2):
        line = []
        for x in range(minx - 1, maxx + 2):
            if (x, y) in image:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))
    print()


if __name__ == '__main__':
    print("part1")
    main("example.txt", 2)
    main("input.txt", 2)
    print()
    print("part2")
    main("example.txt", 50)
    main("input.txt", 50)
