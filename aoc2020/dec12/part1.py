import aocutils


def main(file):
    print("RUNNING", file)
    axis = 0
    direction = 1
    position = [0, 0]
    for line in aocutils.readlines(file):
        inst = line[0]
        a = int(line[1:])
        if inst == "N":
            position[1] += a
        elif inst == "S":
            position[1] -= a
        elif inst == "E":
            position[0] += a
        elif inst == "W":
            position[0] -= a
        elif inst == "F":
            position[axis] += a * direction
        else:
            if a == 180:
                direction = -direction
            elif (inst == "R" and a == 90) or (inst == "L" and a == 270):
                if axis == 0:
                    axis = 1
                    direction = -1 if direction == 1 else 1
                elif axis == 1:
                    axis = 0
            elif (inst == "L" and a == 90) or (inst == "R" and a == 270):
                if axis == 0:
                    axis = 1
                elif axis == 1:
                    axis = 0
                    direction = -1 if direction == 1 else 1
            else:
                assert False
        print(position)
    print(abs(position[0]) + abs(position[1]))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
