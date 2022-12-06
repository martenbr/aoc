import aocutils


def main(file):
    print("RUNNING", file)
    for line in aocutils.readlines(file):
        for i in range(len(line)-3):
            if len(set(line[i:i+4])) == 4:
                print(i+4)
                break


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
