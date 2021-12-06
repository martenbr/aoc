import aocutils


def main(file, simulation_length):
    print("RUNNING", file, f'({simulation_length})')
    line = list(aocutils.readlines(file))[0]
    numbers = [int(x) for x in line.split(',')]
    counts = [0 for _ in range(9)]
    for i in numbers:
        counts[i] += 1

    for day in range(simulation_length):
        new_counts = [counts[i+1] if i != 8 else 0 for i in range(9)]
        new_counts[6] += counts[0]
        new_counts[8] += counts[0]
        counts = new_counts

    print(sum(counts))


if __name__ == '__main__':
    main("example.txt", 16)
    main("example.txt", 80)
    main("example.txt", 256)
    main("input.txt", 80)
    main("input.txt", 256)
