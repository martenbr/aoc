import aocutils


def candidates_from_period(first, distance):
    v = first
    while True:
        yield v
        v += distance


def solve(bus, candidates):
    for t in candidates:
        bus_period, offset = bus
        if (t + offset) % bus_period == 0:
            return t

    assert False


def period_of(bus, candidates):
    # NOTE: Abusing that generators will resume where you left of if you reuse them
    first_t = solve(bus, candidates)
    second_t = solve(bus, candidates)
    period = second_t - first_t
    return first_t, period


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    buses = []
    for i, x in enumerate(lines[1].split(",")):
        if x != 'x':
            buses.append((int(x), i))

    # print(buses)
    bus_period, offset = buses[0]
    first, period = bus_period - offset, bus_period
    for i in range(1, len(buses)):
        first, period = period_of(buses[i], candidates_from_period(first, period))
        # print(buses[:i])
        # print(first, period)
    print(first)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
