import aocutils


def main(file):
    print("RUNNING", file)
    depth = 0
    horizontal = 0
    aim = 0
    for line in aocutils.readlines(file):
        direction, n = line.split(' ', 1)
        n = int(n)
        if direction == 'up':
            aim -= n
        if direction == 'down':
            aim += n
        if direction == 'forward':
            horizontal += n
            depth += n * aim

    print(depth * horizontal)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
