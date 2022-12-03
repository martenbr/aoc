import aocutils


def main(file):
    print("RUNNING", file)
    m = []
    for sec in aocutils.readsections(file):
        a = sum(int(x) for x in sec)
        m.append(a)
    m.sort(reverse=True)
    print(sum(m[0:3]))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
