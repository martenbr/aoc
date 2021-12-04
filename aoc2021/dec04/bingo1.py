import aocutils


def has_won(board, numbers):
    for row in board:
        if all((n in numbers) for n in row):
            return True
    for i in range(5):
        if all((row[i] in numbers) for row in board):
            return True
    return False


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    numbers = [int(x) for x in sections[0][0].split(',')]
    boards = []

    for b in sections[1:]:
        rows = []
        for row in b:
            rows.append([int(x) for x in row.split(' ') if x])

        boards.append(rows)

    play_bingo(boards, numbers)


def play_bingo(boards, numbers):
    drawn_numbers = set()
    for current_draw in numbers:
        drawn_numbers.add(current_draw)

        for board in boards:
            if has_won(board, drawn_numbers):
                s = 0
                for row in board:
                    for n in row:
                        if n not in drawn_numbers:
                            s += n
                print(current_draw)
                print(s)
                print(current_draw * s)
                return


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
