import aocutils


def main(file):
    print("RUNNING", file)
    depth = 0
    horizontal = 0
    for line in aocutils.readlines(file):
        direction, n = line.split(' ', 1)
        n = int(n)
        if direction == 'up':
            depth -= n
        if direction == 'down':
            depth += n
        if direction == 'forward':
            horizontal += n

    print(depth * horizontal)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
