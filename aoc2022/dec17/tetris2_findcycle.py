from collections import defaultdict

import aocutils

PIECES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]


def main(file, num_pieces):
    print("RUNNING", file)
    inputs = next(aocutils.readlines(file))
    piecei = 0
    inputi = 0
    maxy = -1
    seen_outcomes = defaultdict(list)
    board = set()
    outcome = None
    for x in range(0, 7):
        board.add((x, -1))
    for piecenum in range(num_pieces):
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
        if piecei == 0:
            if outcome:
                seen_outcomes[tuple(outcome)].append(piecenum)
            outcome = [inputi]
        piece_parts = PIECES[piecei]
        piecei += 1
        if piecei == len(PIECES):
            piecei = 0
        pos = [(x + 2, y + 4 + maxy) for x, y in piece_parts]
        while True:
            # print(pos)
            inp = inputs[inputi]
            inputi += 1
            if inputi == len(inputs):
                inputi = 0
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
                x, y = pos[0]
                y -= maxy
                outcome.append((x, y))
                new_maxy = max(c[1] for c in pos)
                maxy = max(maxy, new_maxy)
                break
            pos = new_pos

    for v in seen_outcomes.values():
        if len(v) > 2:
            print(v[1]-v[0])
            break


if __name__ == '__main__':
    main("example.txt", 10_000)
    main("input.txt", 10_000)
