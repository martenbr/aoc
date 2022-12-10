import aocutils


def main(file):
    print("RUNNING", file)
    c = 1
    X = 1
    picture = []
    row = []

    def drawpixel():
        pixel = (c - 1) % 40
        sprite = set(range(X - 1, X + 2))
        if pixel in sprite:
            row.append('#')
        else:
            row.append('.')

    for line in aocutils.readlines(file):

        if line == "noop":
            drawpixel()
            if c % 40 == 0:
                picture.append(''.join(row))
                row = []
            c += 1
        else:
            a = int(line.split()[1])
            for _ in range(2):
                drawpixel()
                if c % 40 == 0:
                    picture.append(''.join(row))
                    row = []
                c += 1
            X += a
    while c < 241:
        if c % 40 == 0:
            picture.append(''.join(line))
            line = []
        c += 1
    for l in picture:
        print(l)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
