import aocutils


def main(file):
    print("RUNNING", file)
    for line in aocutils.readlines(file):
        print(line)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
