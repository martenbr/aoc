import aocutils


def main(file):
    print("RUNNING", file)
    score = 0
    for line in aocutils.readlines(file):
        a, b = line.split(" ")
        if a == 'A':
            if b == 'X':
                score += 3
                score += 0
            elif b == 'Y':
                score += 1
                score += 3
            elif b == 'Z':
                score += 2
                score += 6
        elif a == 'B':
            if b == 'X':
                score += 1
                score += 0
            elif b == 'Y':
                score += 2
                score += 3
            elif b == 'Z':
                score += 3
                score += 6
        elif a == 'C':
            if b == 'X':
                score += 2
                score += 0
            elif b == 'Y':
                score += 3
                score += 3
            elif b == 'Z':
                score += 1
                score += 6
    print(score)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
