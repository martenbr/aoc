import aocutils


def pieces():
    while True:
        yield [(0, 0), (1, 0), (2, 0), (3, 0)]
        yield [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
        yield [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
        yield [(0, 0), (0, 1), (0, 2), (0, 3)]
        yield [(0, 0), (0, 1), (1, 0), (1, 1)]


def generate_inputs(line):
    while True:
        yield from line


def main(file, num_pieces):
    print("RUNNING", file)
    input_gen = generate_inputs(next(aocutils.readlines(file)))
    piece_gen = pieces()
    maxy = -1
    board = set()
    for x in range(0, 7):
        board.add((x, -1))
    for _ in range(num_pieces):
        # for y in range(maxy+1, -1, -1):
        #     line = ['|']
        #     for x in range(0, 7):
        #         if (x, y) in board:
        #             line.append('#')
        #         else:
        #             line.append('.')
        #     line.append('|')
        #     print(''.join(line))
        # print("+-------+")
        # print()
        piece_parts = next(piece_gen)
        pos = [(x + 2, y + 4 + maxy) for x, y in piece_parts]
        while True:
            #print(pos)
            inp = next(input_gen)
            if inp == '>':
                new_pos = [(x + 1, y) for x, y in pos]
                if any(c[0] > 6 for c in new_pos) or any((c in board) for c in new_pos):
                    pos = pos
                else:
                    pos = new_pos
            elif inp == '<':
                new_pos = [(x - 1, y) for x, y in pos]
                if any(c[0] < 0 for c in new_pos) or any((c in board) for c in new_pos):
                    pos = pos
                else:
                    pos = new_pos
            else:
                assert False
            new_pos = [(x, y - 1) for x, y in pos]
            if any((c in board) for c in new_pos):
                for c in pos:
                    board.add(c)
                new_maxy = max(c[1] for c in pos)
                maxy = max(maxy, new_maxy)
                break
            pos = new_pos
    print(maxy + 1)


if __name__ == '__main__':
    main("example.txt", 10)  # 17
    main("input.txt", 2022)
