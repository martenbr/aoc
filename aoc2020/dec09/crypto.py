import aocutils


def main(file, window_size):
    print("RUNNING", file)
    numbers = list(int(x) for x in aocutils.readlines(file))
    for i in range(window_size, len(numbers)):
        n = numbers[i]
        recent = numbers[i - window_size:i]
        ok = False
        for p in recent:
            q = (n - p)
            if q in recent:
                ok = True
                break
        if not ok:
            print(n)


if __name__ == '__main__':
    main("example.txt", 5)
    main("input.txt", 25)
