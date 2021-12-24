import functools

import aocutils


def main(file):
    print("RUNNING", file)
    sections = []
    section = []
    for line in aocutils.readlines(file):
        if line == 'inp w':
            section = [line]
            sections.append(section)
        else:
            section.append(line)
    ZDIV_CONST = []
    MOD_OFFSET_CONST = []
    EXTRA_ADD_CONST = []
    for section in sections:
        ZDIV_CONST.append(int(section[4].split(' ')[-1]))
        MOD_OFFSET_CONST.append(int(section[5].split(' ')[-1]))
        EXTRA_ADD_CONST.append(int(section[15].split(' ')[-1]))
    print(MOD_OFFSET_CONST)
    print(ZDIV_CONST)
    print(EXTRA_ADD_CONST)

    def foo(z, w, depth):
        x = z % 26 + MOD_OFFSET_CONST[depth]

        # This is the only place where z can decrease
        # divides by 1 or 26
        z = z // ZDIV_CONST[depth]
        if x != w:
            z = (z * 26) + (w + EXTRA_ADD_CONST[depth])  # Constant is always positive
        return z

    # Determine the maximum z which can lead to a solution (z == 0) after the last step
    # Before the last iteration z must be < 26, the preceding max values
    # can be calculated by multiplying with that iterations ZDIV_CONST
    z_limits_by_depth = [None for _ in range(14)]
    limit = 25
    z_limits_by_depth[13] = limit
    for i in reversed(range(13)):
        limit *= ZDIV_CONST[i]
        z_limits_by_depth[i] = limit
    print(z_limits_by_depth)
    valid_numbers = []
    stack = []

    def find_valid_model_number(z, depth):
        if depth == 14:
            if z == 0:
                valid_numbers.append(int(''.join(str(digit) for digit in stack)))
            return
        if z > z_limits_by_depth[depth]:
            return

        for w in range(1, 10):
            new_z = foo(z, w, depth)
            stack.append(w)
            find_valid_model_number(new_z, depth + 1)
            stack.pop()

    find_valid_model_number(0, 0)
    print(max(valid_numbers))
    print(min(valid_numbers))


if __name__ == '__main__':
    main("input.txt")
