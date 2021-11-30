import itertools


def main(input, moves):
    print("RUNNING", input)

    cups = [int(c) for c in input]
    current_cup = cups[0]
    ci = 0
    for _ in range(moves):
        begin = ci + 1
        end = ci + 4
        if end > 9:
            end = end - 9
            picked = list(itertools.chain(
                cups[begin:],
                cups[:end],
            ))
        else:
            picked = cups[begin:end]
        destination_cup = current_cup - 1
        while True:
            if destination_cup == 0:
                destination_cup += 9
            if destination_cup not in picked:
                break
            destination_cup -= 1

        destination_index = index_of(cups, destination_cup)
        if begin < end and destination_index < end:
            # 1 (2) 3 [4 5 6] 7
            new_cups = list(itertools.chain(
                cups[:destination_index+1],
                picked,
                cups[destination_index+1:begin],
                cups[end:],
            ))
        elif begin < end and destination_index >= end:
            # 1 [2 3 4] 5 (6) 7
            new_cups = list(itertools.chain(
                cups[:begin],
                cups[end:destination_index + 1],
                picked,
                cups[destination_index+1:],
            ))
        else:
            # 1 2] 3 4 (5) 6 [7
            new_cups = list(itertools.chain(
                cups[end:destination_index + 1],
                picked,
                cups[destination_index+1:begin],
            ))
        cups = new_cups
        ci = index_of(cups, current_cup)
        ci += 1
        if ci == 9:
            ci = 0
        current_cup = cups[ci]
    i = index_of(cups, 1)
    seq = list(itertools.chain(
        cups[i+1:],
        cups[:i],
    ))
    print("".join(str(c) for c in seq))


def index_of(cups, destination_cup):
    for i, c in enumerate(cups):
        if c == destination_cup:
            return i
    assert False


if __name__ == '__main__':
    main("389125467", 100)
    main("362981754", 100)
