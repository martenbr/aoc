import aocutils


def main(file):
    print("RUNNING", file)
    lines = [int(l) for l in aocutils.readlines(file)]
    lines.sort()
    lines.append(lines[-1] + 3)
    groups_of_ones = []
    prev = 0
    ones_in_a_row = 0
    for jole in lines:
        diff = jole - prev
        prev = jole
        if diff == 1:
            ones_in_a_row += 1
        else:
            groups_of_ones.append(ones_in_a_row)
            ones_in_a_row = 0
    groups_of_ones.append(ones_in_a_row)
    groups_of_ones = [ones for ones in groups_of_ones if ones > 1]
    combs = 1
    for ones in groups_of_ones:
        if ones == 2:
            # (1) 2 (3)
            # (1) - (3)
            combs *= 2
        elif ones == 3:
            # (1) 2 3 (4)
            # (1) 2 - (4)
            # (1) - 3 (4)
            # (1) - - (4)
            combs *= 4
        elif ones == 4:
            # (1) 2 3 4 (5)
            # (1) 2 3 - (5)
            # (1) 2 - 4 (5)
            # (1) 2 - - (5)
            # (1) - 3 4 (5)
            # (1) - 3 - (5)
            # (1) - - 4 (5)
            combs *= 7
        else:
            assert False, "Not my problem(input)"
    print(combs)


if __name__ == '__main__':
    main("example.txt")
    main("example2.txt")
    main("input.txt")
