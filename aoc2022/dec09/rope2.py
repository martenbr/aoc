import aocutils


def main(file):
    print("RUNNING", file)
    visited = {(0, 0)}
    rope = [(0, 0) for _ in range(10)]
    for line in aocutils.readlines(file):
        d, cnt = line.split(' ')
        cnt = int(cnt)
        for _ in range(cnt):
            hx, hy = rope[0]
            if d == 'U':
                hy += 1
            elif d == 'D':
                hy -= 1
            elif d == 'R':
                hx += 1
            elif d == 'L':
                hx -= 1
            rope[0] = (hx, hy)
            for i in range(1, 10):
                hx, hy = rope[i - 1]
                tx, ty = rope[i]
                if abs(hx - tx) > 1 or abs(hy - ty) > 1:
                    if tx < hx:
                        tx += 1
                    elif tx > hx:
                        tx -= 1
                    if ty < hy:
                        ty += 1
                    elif ty > hy:
                        ty -= 1
                    rope[i] = (tx, ty)
            visited.add(rope[-1])
    print(len(visited))


if __name__ == '__main__':
    main("example.txt")
    main("example2.txt")
    main("input.txt")
