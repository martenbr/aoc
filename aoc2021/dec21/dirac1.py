import aocutils


def deterministic_rolls():
    i = 1
    while True:
        if i < 98:
            yield i * 3 + 3
            i += 3
        else:
            s = 0
            for _ in range(3):
                s += i
                i += 1
                if i > 100:
                    i = 1
            yield s

def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    p1 = int(lines[0][-1])
    p2 = int(lines[1][-1])
    dice = deterministic_rolls()
    p1_score = 0
    p2_score = 0
    for i in range(9999):
        roll = next(dice)
        p1 = ((p1 + roll - 1) % 10) + 1
        p1_score += p1
        if p1_score >= 1000:
            print(p2_score, '*', (i * 6 + 3))
            print(p2_score * (i * 6 + 3))
            return

        roll = next(dice)
        p2 = ((p2 + roll - 1) % 10) + 1
        p2_score += p2
        if p2_score >= 1000:
            print(p1_score, '*', (i * 6 + 6))
            print(p1_score * (i * 6 + 6))
            return


if __name__ == '__main__':
    main("example.txt")
    print(739785, "expected")
    main("input.txt")
