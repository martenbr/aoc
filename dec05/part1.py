def main():
    taken = []
    for line in open("input.txt"):
        taken.append(decode(line.strip()))
    taken.sort()
    x, y = taken[-1]
    print(x * 8 + y)


def decode(input):
    row_part = input[:7]
    column_part = input[7:]
    row = decode_row(row_part)
    col = decode_col(column_part)
    return row, col


def decode_row(row_part):
    min_row = 0
    max_row = 127
    for c in row_part:
        half = (max_row - min_row) // 2
        if c == "F":
            max_row = min_row + half
        elif c == "B":
            min_row = max_row - half
        else:
            assert False
    row = max_row
    return row


def decode_col(column_part):
    min_col = 0
    max_col = 7
    for c in column_part:
        half = ((max_col - min_col) // 2)
        if c == "L":
            max_col = min_col + half
        elif c == "R":
            min_col = max_col - half
        else:
            assert False
    col = max_col
    return col


if __name__ == '__main__':
    main()
