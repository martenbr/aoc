import heapq
from typing import List


def readsections(file):
    return sections_from_lines(open(file))


def readlines(file):
    for line in open(file):
        yield line.strip('\r\n')


def multisplit(line: str, tokens: List[str]):
    rest = line
    parts = []
    for t in tokens:
        p1, rest = rest.split(t, 1)
        parts.append(p1)
    parts.append(rest)
    return parts


def sections_from_lines(lines):
    section = []
    for line in lines:
        line = line.strip('\r\n')
        if line == "":
            yield section
            section = []
        else:
            section.append(line)
    if section:
        yield section


def dijkstra(neighbors, start, dest):
    costs = {}
    q = [(0, start)]
    while q:
        cost, node = heapq.heappop(q)
        if node == dest:
            return cost
        for edge_cost, node in neighbors(node):
            new_cost = cost + edge_cost
            if node in costs and costs[node] <= new_cost:
                continue
            costs[node] = new_cost
            heapq.heappush(q, (new_cost, node))
    assert False