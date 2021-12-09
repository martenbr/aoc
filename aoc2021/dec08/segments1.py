import aocutils


def main(file):
    print("RUNNING", file)
    cnt = 0
    for line in aocutils.readlines(file):
        out = line.split(' | ')[1]
        for digit in out.split(' '):
            if len(digit) in [2, 3, 4, 7]:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
