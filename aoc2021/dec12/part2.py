from collections import defaultdict
from dataclasses import dataclass
from typing import List

import aocutils

neighbors = defaultdict(list)


@dataclass
class State:
    visited: List[str]
    paths: int = 0
    double_visit: bool = False


def visit(state, node):
    state.visited.append(node)
    if node == 'end':
        state.paths += 1
    else:
        for n in neighbors[node]:
            if n.isupper():
                visit(state, n)
            elif n not in state.visited:
                visit(state, n)
            elif not state.double_visit and n != 'start':
                state.double_visit = True
                visit(state, n)
                state.double_visit = False
    state.visited.pop()


def main(file):
    print("RUNNING", file)
    neighbors.clear()
    for line in aocutils.readlines(file):
        a, b = line.split('-')
        neighbors[a].append(b)
        neighbors[b].append(a)
    state = State([])
    visit(state, 'start')
    print(state.paths)


if __name__ == '__main__':
    main("example.txt")
    print("== 36")
    main("example2.txt")
    print("== 103")
    main("example3.txt")
    print("== 3509")
    main("input.txt")
