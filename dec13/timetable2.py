import aocutils


def candidates_from_period(first, period):
    v = first
    while True:
        yield v
        v += period


def find_solutions(bus, candidates):
    for t in candidates:
        bus_period, offset = bus
        if (t + offset) % bus_period == 0:
            yield t


def period_of(bus, candidates):
    solutions = find_solutions(bus, candidates)
    first_t = next(solutions)
    second_t = next(solutions)
    period = second_t - first_t
    return first_t, period


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    buses = []
    for offset, number in enumerate(lines[1].split(",")):
        if number != 'x':
            buses.append((int(number), offset))

    bus_period, offset = buses[0]
    first_t, period = bus_period - offset, bus_period
    for bus in buses[1:]:
        first_t, period = period_of(bus, candidates_from_period(first_t, period))
    print(first_t)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
