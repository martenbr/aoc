import aocutils


def main(file):
    print("RUNNING", file)
    cnt = 0
    prev = None
    for line in aocutils.readlines(file):
        a = int(line)
        if prev is not None:
            if a > prev:
                cnt += 1
        prev = a

    print(cnt)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
