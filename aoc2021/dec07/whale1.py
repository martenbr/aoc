import aocutils


def total_fuel_cost(p, positions):
    return sum(abs(x - p) for x in positions)


def main(file):
    print("RUNNING", file)
    line = list(aocutils.readlines(file))[0]
    positions = [int(x) for x in line.split(',')]
    sortedp = sorted(positions)
    p0 = sortedp[len(sortedp) // 2]
    p1 = p0 + 1
    c0 = total_fuel_cost(p0, positions)
    c1 = total_fuel_cost(p1, positions)
    if c0 > c1:
        start = p1
        cost = c1
        dir = 1
    else:
        start = p0
        cost = c0
        dir = -1
    pos = start
    while True:
        nextp = pos + dir
        nextc = total_fuel_cost(nextp, positions)
        if nextc > cost:
            break
        pos = nextp
        cost = nextc
    print(pos)
    print(cost)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
