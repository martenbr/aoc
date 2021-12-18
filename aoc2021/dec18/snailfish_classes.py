import json
from dataclasses import dataclass
from typing import Optional, Tuple, List, Union

import aocutils
import copy


def main_part1(file):
    print("RUNNING", "part1", file)
    numbers = [json.loads(line) for line in aocutils.readlines(file)]
    curr = make_number(numbers[0])
    for n in numbers[1:]:
        curr = Pair(curr, make_number(n))
        reduce(curr)
    print(curr.magnitude())


def main_part2(file):
    print("RUNNING", "part2", file)
    numbers = [json.loads(line) for line in aocutils.readlines(file)]
    max_magnitude = 0
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers):
            if i != j:
                max_magnitude = max(max_magnitude, add(n1, n2).magnitude())
    print(max_magnitude)


def add(n1, n2):
    num = make_number([n1, n2])
    reduce(num)
    return num


def make_number(n):
    if isinstance(n, int):
        return Num(n)
    else:
        return Pair(make_number(n[0]), make_number(n[1]))


@dataclass
class State:
    prev_number: Optional['Num']


@dataclass
class Num:
    value: int

    def push_value(self, n: int):
        self.value += n

    def explode(self, depth, state: State) -> Optional[int]:
        state.prev_number = self
        return None

    def split(self):
        if self.value >= 10:
            n, rest = divmod(self.value, 2)
            return Pair(Num(n), Num(n + rest))

    def magnitude(self):
        return self.value

    def __repr__(self):
        return str(self.value)


@dataclass
class Pair:
    left: Union['Pair', Num]
    right: Union['Pair', Num]

    def push_value(self, n: int):
        self.left.push_value(n)

    def explode(self, depth, state: State) -> Optional[int]:
        if depth == 3:
            if isinstance(self.left, Pair):
                l = self.left.left
                r = self.left.right
                assert isinstance(l, Num)
                assert isinstance(r, Num)
                if state.prev_number is not None:
                    state.prev_number.value += l.value
                self.left = Num(0)
                self.right.push_value(r.value)
                raise Modified
            elif isinstance(self.right, Pair):
                l = self.right.left
                r = self.right.right
                assert isinstance(l, Num)
                assert isinstance(r, Num)
                self.left.value += l.value
                self.right = Num(0)
                return r.value

        n = self.left.explode(depth + 1, state)
        if n is not None:
            self.right.push_value(n)
            raise Modified
        return self.right.explode(depth + 1, state)

    def split(self):
        if new_left := self.left.split():
            self.left = new_left
            raise Modified
        if new_right := self.right.split():
            self.right = new_right
            raise Modified

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __repr__(self):
        return f'[{self.left!r},{self.right!r}]'


class Modified(Exception):
    pass


def reduce(num: Pair):
    while True:
        try:
            # First try explode
            leftover = num.explode(0, State(None))
            if leftover:
                # A number was exploded but there was nothing to the right side
                continue

            # If nothing to explode try a split
            top_level_modified = num.split()
            assert not top_level_modified

            # Can't explode or split, number is fully reduced
            break
        except Modified:
            continue


if __name__ == '__main__':
    main_part1("example.txt")
    print(4140, "expected")
    main_part1("input.txt")

    print()
    main_part2("example.txt")
    print(3993, "expected")
    main_part2("input.txt")
