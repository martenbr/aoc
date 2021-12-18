import json
from dataclasses import dataclass
from typing import Optional, Tuple, List

import aocutils
import copy


def main_part1(file):
    print("RUNNING", "part1", file)
    numbers = [json.loads(line) for line in aocutils.readlines(file)]
    curr = numbers[0]
    for n in numbers[1:]:
        curr = [curr, n]
        reduce(curr)
    # print(curr)
    print(magnitude(curr))


def main_part2(file):
    print("RUNNING", "part2", file)
    numbers = [json.loads(line) for line in aocutils.readlines(file)]
    max_magnitude = 0
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers):
            if i != j:
                max_magnitude = max(max_magnitude, magnitude(add(n1, n2)))
    print(max_magnitude)


def add(n1, n2):
    res = [copy.deepcopy(n1), copy.deepcopy(n2)]
    reduce(res)
    return res


@dataclass
class State:
    recent_number: Optional[Tuple[List[int], int]]


def magnitude(num):
    if isinstance(num, int):
        return num
    else:
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


def push_value(num, side, val):
    if isinstance(num[side], int):
        num[side] += val
    else:
        push_value(num[side], 0, val)


class Modified(Exception):
    pass


def explode(num, depth, state: State):
    if depth == 3:
        if isinstance(num[0], list):
            l, r = num[0]
            assert isinstance(l, int)
            assert isinstance(r, int)
            num[0] = 0
            if state.recent_number is not None:
                left_number, side = state.recent_number
                left_number[side] += l
            push_value(num, 1, r)
            raise Modified
        elif isinstance(num[1], list):
            l, r = num[1]
            assert isinstance(l, int)
            assert isinstance(r, int)
            num[0] += l
            num[1] = 0
            return r
        else:
            state.recent_number = (num, 1)
            return None

    else:
        if isinstance(num[0], int):
            state.recent_number = (num, 0)
        else:
            n = explode(num[0], depth + 1, state)
            if n is not None:
                push_value(num, 1, n)
                raise Modified
        if isinstance(num[1], int):
            state.recent_number = (num, 1)
        else:
            n = explode(num[1], depth + 1, state)
            return n

        return None


def split_first(num):
    if isinstance(num, int):
        if num >= 10:
            n, rest = divmod(num, 2)
            return [n, n + rest]
        else:
            return None
    if new_elem := split_first(num[0]):
        num[0] = new_elem
        raise Modified
    if new_elem := split_first(num[1]):
        num[1] = new_elem
        raise Modified


def reduce(num):
    while True:
        try:
            # First try explode
            n = explode(num, 0, State(None))
            if n:
                # A number was exploded but there was nothing to the right side
                continue

            # If nothing to explode try a split
            top_level_modified = split_first(num)
            assert not top_level_modified

            # Can't explode or split, number is fully reduced
            break
        except Modified:
            continue


if __name__ == '__main__':
    main_part1("example.txt")
    print(4140, "expected")
    main_part1("input.txt")

    main_part2("example.txt")
    print(3993, "expected")
    main_part2("input.txt")
