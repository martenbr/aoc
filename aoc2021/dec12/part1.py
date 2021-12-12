from collections import defaultdict

import aocutils

neighbors = defaultdict(list)

paths = []

def visit(node, visited):
    visited.append(node)
    if node == 'end':
        paths.append(visited.copy())
    else:
        for n in neighbors[node]:
            if n.isupper() or n not in visited:
                visit(n, visited)
    visited.pop()


def main(file):
    neighbors.clear()
    paths.clear()
    print("RUNNING", file)
    for line in aocutils.readlines(file):
        a, b = line.split('-')
        neighbors[a].append(b)
        neighbors[b].append(a)
    visited = list()
    visit('start', visited)
    print(len(paths))


if __name__ == '__main__':
    main("example.txt")
    print("== 10")
    main("example2.txt")
    print("== 19")
    main("example3.txt")
    print("== 226")
    main("input.txt")
