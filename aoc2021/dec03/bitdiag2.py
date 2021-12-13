import aocutils


def main(file):
    print("RUNNING", file)

    lines = list(aocutils.readlines(file))
    samples = [(int(l, base=2), l) for l in lines]
    for i in reversed(list(range(len(lines[0])))):
        if len(samples) == 1:
            break
        ones, zeros = count_ones_and_zeros(samples)
        mask = 1 << i
        if ones[i] >= zeros[i]:
            samples = [(num, bitstr) for num, bitstr in samples if num & mask != 0]
        else:
            samples = [(num, bitstr) for num, bitstr in samples if num & mask == 0]

    print(samples)
    oxy = samples[0][0]

    samples = [(int(l, base=2), l) for l in lines]
    for i in reversed((range(len(lines[0])))):
        if len(samples) == 1:
            break
        ones, zeros = count_ones_and_zeros(samples)
        mask = 1 << i
        if ones[i] >= zeros[i]:
            samples = [(l, b) for l, b in samples if l & mask == 0]
        else:
            samples = [(l, b) for l, b in samples if l & mask != 0]
    print(samples)
    co2 = samples[0][0]

    print(co2 * oxy)


def count_ones_and_zeros(samples):
    zeros = [0 for _ in samples[0][1]]
    ones = [0 for _ in samples[0][1]]
    for num, bitstr in samples:
        for i, bit in enumerate(bitstr):
            if bit == '1':
                ones[i] += 1
            else:
                zeros[i] += 1
    ones.reverse()
    zeros.reverse()
    return ones, zeros


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
