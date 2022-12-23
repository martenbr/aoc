import aocutils


def main(file):
    print("RUNNING", file)
    grid = [None]
    play_area_by_y = [(0, 0)]
    play_area_by_x = [(0, 0)]
    sections = list(aocutils.readsections(file))
    for line0 in sections[0]:
        line = ' ' + line0 + ' '
        grid.append(line)
        stripped = line.strip()
        start = line.find(stripped[0])
        length = len(stripped)
        play_area_by_y.append((start, start + length - 1))
    grid[0] = ''
    rowlen = max(len(l) for l in grid)
    blank_line = ' ' * rowlen
    grid[0] = blank_line
    grid.append(blank_line)
    for y in range(len(grid)):
        grid[y] = grid[y].ljust(rowlen, ' ')
        assert len(grid[y]) == rowlen
    for x in range(1, len(grid[0]) - 1):
        column = []
        for y in range(len(grid)):
            column.append(grid[y][x])
        col = ''.join(column)
        stripped = col.strip()
        start = col.find(stripped[0])
        length = len(stripped)
        play_area_by_x.append((start, start + length - 1))

    i = 0
    instr_line = sections[1][0]
    instructions = []
    was_digit = True
    for j in range(len(instr_line)):
        is_digit = instr_line[j].isdigit()
        if is_digit == was_digit:
            pass
        else:
            instructions.append(instr_line[i:j])
            i = j
        was_digit = is_digit

    instructions.append(instr_line[i:])

    y = 1
    x = play_area_by_y[y][0]
    face = 0
    for inst in instructions:
        if inst == 'R':
            face = (face + 1) % 4
        elif inst == 'L':
            face = (face - 1) % 4
        else:
            steps = int(inst)
            if face == 0:
                wrapx, _ = play_area_by_y[y]
                for _ in range(steps):
                    targetx = x + 1
                    if grid[y][targetx] == ' ':
                        targetx = wrapx
                    if grid[y][targetx] == '.':
                        x = targetx
                    elif grid[y][targetx] == '#':
                        pass
                    else:
                        assert False
            elif face == 1:
                wrapy, _ = play_area_by_x[x]
                for _ in range(steps):
                    targety = y + 1
                    if grid[targety][x] == ' ':
                        targety = wrapy
                    if grid[targety][x] == '.':
                        y = targety
                    elif grid[targety][x] == '#':
                        pass
                    else:
                        assert False
            elif face == 2:
                _, wrapx = play_area_by_y[y]
                for _ in range(steps):
                    targetx = x - 1
                    if grid[y][targetx] == ' ':
                        targetx = wrapx
                    if grid[y][targetx] == '.':
                        x = targetx
                    elif grid[y][targetx] == '#':
                        pass
                    else:
                        assert False
            elif face == 3:
                _, wrapy = play_area_by_x[x]
                for _ in range(steps):
                    targety = y - 1
                    if grid[targety][x] == ' ':
                        targety = wrapy
                    if grid[targety][x] == '.':
                        y = targety
                    elif grid[targety][x] == '#':
                        pass
                    else:
                        assert False

    print(1000 * y + 4 * x + face)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
