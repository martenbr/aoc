import heapq
from collections import defaultdict

import aocutils


def main(file):
    def distp(node):
        return [(1, n) for n in neighbors[node]]

    print("RUNNING", file)
    neighbors = {}
    flows = {}
    for line in aocutils.readlines(file):
        splits = line.split(' ', 9)
        valve = splits[1]
        flow = aocutils.parseints(splits[4])[0]
        paths = splits[9].split(', ')
        flows[valve] = flow
        neighbors[valve] = paths
    maxflow = sum(flow for flow in flows.values())

    dists = defaultdict(dict)
    interesting = {n for n in neighbors.keys() if flows[n]}
    for n in interesting:
        for othern, dist in aocutils.dijkstra(distp, n, None).items():
            if othern in interesting:
                dists[n][othern] = dist
    for othern, dist in aocutils.dijkstra(distp, 'AA', None).items():
        if othern in interesting:
            dists['AA'][othern] = dist
    states = [(0, 0, 'AA', [], 0, 0)]
    best = 0
    while states:
        missed, t, node, opened, flow, total = heapq.heappop(states)
        for n, dist in dists[node].items():
            if n in opened:
                continue
            time_taken = dist + 1
            if t + time_taken > 30:
                continue

            new_missed = missed + (maxflow - flow) * time_taken
            new_flow = flow + flows[n]
            new_opened = list(opened)
            new_opened.append(n)
            new_total = total + time_taken * flow
            heapq.heappush(
                states,
                (new_missed, t + time_taken, n, new_opened, new_flow, new_total),
            )
            current_potential = new_total + (30 - t - time_taken) * new_flow
            if current_potential > best:
                best = current_potential
    print(best)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
