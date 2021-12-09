import aocutils


def main(file):
    print("RUNNING", file)
    map = []
    for line in aocutils.readlines(file):
        map.append(([int(x) for x in line]))
    danger = 0
    for y, row in enumerate(map):
        for x, v in enumerate(row):
            if x != 0:
                if v >= row[x-1]:
                    continue
            if x != len(row) - 1:
                if v >= row[x + 1]:
                    continue
            if y != 0:
                if v >= map[y-1][x]:
                    continue

            if y != len(map) - 1:
                if v >= map[y + 1][x]:
                    continue
            danger += v + 1
    print(danger)

if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
