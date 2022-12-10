import aocutils


def main(file):
    print("RUNNING", file)
    c = 1
    v = 0
    X = 1
    for line in aocutils.readlines(file):
        if line == "noop":
            if (c + 20) % 40 == 0:
                v += X * c
            c += 1
        else:
            a = int(line.split()[1])
            for _ in range(2):
                if (c + 20) % 40 == 0:
                    v += X * c
                c += 1
            X += a
    while c < 221:
        if (c + 20) % 40 == 0:
            v += X * c
        c += 1

    print(v)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
