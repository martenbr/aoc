import aocutils


def main(file):
    print("RUNNING", file)
    x = 0
    y = 1
    vec = [10, 1]
    position = [0, 0]
    for line in aocutils.readlines(file):
        inst = line[0]
        a = int(line[1:])
        if inst == "N":
            vec[y] += a
        elif inst == "S":
            vec[y] -= a
        elif inst == "E":
            vec[x] += a
        elif inst == "W":
            vec[x] -= a
        elif inst == "F":
            position[x] += vec[x] * a
            position[y] += vec[y] * a
        elif inst in ["L", "R"]:
            if a == 180:
                vec[x], vec[y] = -vec[x], -vec[y]
            else:
                if inst == "L":
                    a = 360 - a
                if a == 90:
                    vec[x], vec[y] = vec[y], -1 * vec[x]
                elif a == 270:
                    vec[x], vec[y] = -1 * vec[y], vec[x]
                else:
                    assert False
        else:
            assert False
        print(position, vec)
    print(abs(position[x]) + abs(position[y]))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
