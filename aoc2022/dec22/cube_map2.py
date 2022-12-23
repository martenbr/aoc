import math

import aocutils

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def follow_warp(grid, warps, gatex, gatey, face):
    (newx, newy), newdir = warps[((gatex, gatey), face)]

    # We are still "inside" the warp point, step out of it
    newx2, newy2, newdir2 = step(grid, warps, newx, newy, newdir)
    assert newdir == newdir2
    if newx == newx2 and newy == newy2:
        return None  # We hit a wall
    tile = grid[newy2][newx2]
    if tile == '.':
        return newx2, newy2, newdir2
    else:
        assert False


def step(grid, warps, x, y, face):
    if face == RIGHT:
        targetx = x + 1
        targety = y
    elif face == LEFT:
        targetx = x - 1
        targety = y
    elif face == DOWN:
        targetx = x
        targety = y + 1
    elif face == UP:
        targetx = x
        targety = y - 1
    else:
        assert False
    if grid[targety][targetx] == ' ':
        result = follow_warp(grid, warps, targetx, targety, face)
        if result is None:
            return x, y, face  # We hit a wall
        return result
    elif grid[targety][targetx] == '.':
        return targetx, targety, face
    elif grid[targety][targetx] == '#':
        return x, y, face
    else:
        assert False


def main(file, sides, connections):
    print("RUNNING", file)
    grid = ['']
    sections = list(aocutils.readsections(file))
    for line in sections[0]:
        grid.append(' ' + line + ' ')
    rowlen = max(len(l) for l in grid)
    blank_line = ' ' * rowlen
    grid[0] = blank_line
    grid.append(blank_line)
    for y in range(len(grid)):
        grid[y] = grid[y].ljust(rowlen, ' ')
        assert len(grid[y]) == rowlen

    def get_edge(side, direction):
        xstart, ystart = sides[side]
        if direction in (UP, DOWN):
            if direction == UP:
                y = ystart - 1
            else:
                y = ystart + 50
            return [(x, y) for x in range(xstart, xstart + 50)]
        else:
            if direction == LEFT:
                x = xstart - 1
            else:
                x = xstart + 50
            return [(x, y) for y in range(ystart, ystart + 50)]

    warps = {}
    for face1, dir1, face2, dir2, inverted in connections:
        edge1 = get_edge(face1, dir1)
        edge2 = get_edge(face2, dir2)
        if inverted:
            edge2 = reversed(edge2)
        for c1, c2 in zip(edge1, edge2):
            warps[(c1, dir1)] = (c2, (dir2 + 2) % 4)
            warps[(c2, dir2)] = (c1, (dir1 + 2) % 4)
    assert warps[((50, 1), LEFT)] == ((0, 150), RIGHT)
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
    x = grid[y].find('.')
    face = 0

    for inst in instructions:
        if inst == 'R':
            face = (face + 1) % 4
        elif inst == 'L':
            face = (face - 1) % 4
        else:
            steps = int(inst)
            for _ in range(steps):
                x, y, face = step(grid, warps, x, y, face)

    print(1000 * y + 4 * x + face)


if __name__ == '__main__':
    # main("example.txt")
    main("input.txt", sides={
        # upper left coordinate contained in a cube face
        'a': (51, 1),
        'b': (101, 1),
        'c': (51, 51),
        'd': (1, 101),
        'e': (51, 101),
        'f': (1, 151),
    }, connections=[
        # cube face connections
        ('a', LEFT, 'd', LEFT, True),
        ('a', UP, 'f', LEFT, False),
        ('b', UP, 'f', DOWN, False),
        ('b', RIGHT, 'e', RIGHT, True),
        ('b', DOWN, 'c', RIGHT, False),
        ('c', LEFT, 'd', UP, False),
        ('e', DOWN, 'f', RIGHT, False),
    ])
