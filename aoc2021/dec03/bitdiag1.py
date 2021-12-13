import aocutils


def main(file):
    print("RUNNING", file)
    zeros = None
    ones = None
    for line in aocutils.readlines(file):
        if zeros is None:
            zeros = [0 for _ in line]
            ones = [0 for _ in line]
        for i, bit in enumerate(line):
            if bit == '1':
                ones[i] += 1
            else:
                zeros[i] += 1

    gamma = 0
    epsilon = 0
    for i in range(len(ones)):
        gamma = gamma << 1
        epsilon = epsilon << 1
        if ones[i] > zeros[i]:
            gamma |= 1
        else:
            epsilon |= 1
    print(gamma, epsilon)
    print(gamma * epsilon)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
