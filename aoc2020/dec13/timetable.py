import aocutils


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    departure = int(lines[0])
    in_service = []
    for x in lines[1].split(","):
        if x != 'x':
            in_service.append(int(x))

    for i in range(departure, departure + 1_000_000):
        for bus in in_service:
            if i % bus == 0:
                print(bus, departure, i - departure)
                print((i - departure) * bus)
                return


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
