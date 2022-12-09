import aocutils


def main(file):
    print("RUNNING", file)
    hx = 0
    hy = 0
    ty = 0
    tx = 0
    visited = {(0, 0)}
    for line in aocutils.readlines(file):
        d, cnt = line.split(' ')
        cnt = int(cnt)
        for _ in range(cnt):
            if d == 'U':
                hy += 1
            elif d == 'D':
                hy -= 1
            elif d == 'R':
                hx += 1
            elif d == 'L':
                hx -= 1
            if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                if tx < hx:
                    tx += 1
                elif tx > hx:
                    tx -= 1
                if ty < hy:
                    ty += 1
                elif ty > hy:
                    ty -= 1
                visited.add((tx, ty))
    print(len(visited))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
