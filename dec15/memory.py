import aocutils


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    line = lines[0]
    numbers = line.split(",")
    numbers = [int(n) for n in numbers]
    t = 1
    prev = None
    times = dict()
    while True:
        if t <= len(numbers):
            current = numbers[t - 1]
        else:
            ts = times.get(prev, None)
            if ts is None:
                current = 0
            else:
                current = t - ts - 1

        if t == 2020:
            print("2020: ", current)

        if t == 30000000:
            print("30,000,000:", current)
            break

        if prev is not None:
            # print(t - 1, prev)
            times[prev] = t - 1
        prev = current
        t += 1


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
