import aocutils


def main(file):
    print("RUNNING", file)
    numbers = []
    for line in aocutils.readlines(file):
        numbers.append(parse_snafu(line))
    num = sum(numbers)
    digits = 1
    while True:
        if parse_snafu('1' + ('=' * (digits - 1))) > num:
            digits -= 1
            break
        digits += 1
    snafu = ['2' for _ in range(digits)]
    for i in range(digits):
        for c in ('=', '-', '0', '1', '2'):
            snafu[i] = c
            if parse_snafu(''.join(snafu)) >= num:
                break
    snafu_number = ''.join(snafu)
    print(parse_snafu(snafu_number), '==', num)
    print(snafu_number)


def parse_snafu(line):
    num = 0
    multi = 1
    for c in reversed(line):
        if c == '-':
            n = -1
        elif c == '=':
            n = -2
        else:
            n = int(c)
        num += n * multi
        multi *= 5
    return num


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")  # 20-1-11==0-=0112-222
