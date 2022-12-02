import aocutils


def main(file):
    print("RUNNING", file)
    m = []
    for sec in aocutils.readsections(file):
        a = sum(int(x)for x in sec)
        m = max(m, a)
    print(m)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
