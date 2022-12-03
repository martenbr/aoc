import aocutils


def main(file):
    print("RUNNING", file)
    score = 0
    for line in aocutils.readlines(file):
        a, b = line.split(" ")
        if a == 'A':
            if b == 'X':
                move = 1
                rnd = 3
            elif b == 'Y':
                move = 2
                rnd = 6
            elif b == 'Z':
                move = 3
                rnd = 0
        elif a == 'B':
            if b == 'X':
                move = 1
                rnd = 0
            elif b == 'Y':
                move = 2
                rnd = 3
            elif b == 'Z':
                move = 3
                rnd = 6
        elif a == 'C':
            if b == 'X':
                move = 1
                rnd = 6
            elif b == 'Y':
                move = 2
                rnd = 0
            elif b == 'Z':
                move = 3
                rnd = 3
        score += (rnd + move)
    print(score)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
