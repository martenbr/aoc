import aocutils


def main(file, preamble_count):
    print("RUNNING", file)
    numbers = list(int(x) for x in aocutils.readlines(file))
    weakness = find_weakness(numbers, preamble_count)
    assert weakness is not None
    print(weakness)
    for i in range(len(numbers)):
        x = numbers[i]
        for j in range(i + 1, len(numbers)):
            x += numbers[j]
            if x > weakness:
                break
            elif x == weakness:
                ns = numbers[i:j + 1]
                print(max(ns) + min(ns))
                return


def find_weakness(numbers, window_size):
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
            return n
            break
    return None


if __name__ == '__main__':
    main("example.txt", 5)
    main("input.txt", 25)
