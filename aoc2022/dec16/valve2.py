import heapq
from collections import defaultdict

import aocutils


def step_time(maxflow, flows, state):
    if state[3] > 0 and state[5] > 0:
        missed, t, node, remaining, enode, ermaining, opened, flow, total = state
        future = flow * t
        if node != 'IDLE':
            assert remaining <= t
            future += (t - remaining) * flows[node]
        if enode != 'IDLE':
            assert ermaining <= t
            future += (t - ermaining) * flows[enode]
        new_missed = maxflow * 26 - total - future
        stept = min(remaining, ermaining, t)
        new_total = total + flow * stept

        return new_missed, t - stept, node, remaining - stept, enode, ermaining - stept, opened, flow, new_total
    else:
        return state


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
                if othern != n:
                    dists[n][othern] = dist
    for othern, dist in aocutils.dijkstra(distp, 'AA', None).items():
        if othern in interesting:
            dists['AA'][othern] = dist
    dists['IDLE'] = dict()

    bitfornode = {n: 1 << i for i, n in enumerate(interesting)}
    states = [(maxflow * 26, 26, 'AA', 0, 'AA', 0, 0, 0, 0)]
    best = 0
    mint = 0
    while states:
        missed, t, node, remaining, enode, ermaining, opened, flow, total = heapq.heappop(states)
        if t < mint:
            mint = t
            print(f"t={t} states={len(states)}")
        if node == 'IDLE' and enode == 'IDLE':
            final_value = total + t * flow
            if final_value > best:
                best = final_value
            continue

        # TODO tighter upper bound
        best_possible_result = total + t * maxflow
        if best_possible_result < best:
            continue

        if remaining == 0:
            new_flow = flow + flows[node]
            actions = 0
            for n, dist in dists[node].items():
                if bitfornode[n] & opened != 0:
                    continue
                action_time = dist + 1
                if t - action_time < 0:
                    continue
                actions += 1
                heapq.heappush(
                    states,
                    step_time(maxflow, flows, (missed, t, n, action_time, enode, ermaining, opened | bitfornode[n], new_flow, total)),
                )
            if actions < 2:
                heapq.heappush(
                    states,
                    step_time(maxflow, flows, (missed, t, 'IDLE', 99, enode, ermaining, opened, new_flow, total))
                )
        elif ermaining == 0:
            new_flow = flow + flows[enode]
            actions = 0
            for n, dist in dists[enode].items():
                if bitfornode[n] & opened != 0:
                    continue
                action_time = dist + 1
                if t - action_time < 0:
                    continue

                actions += 1
                heapq.heappush(
                    states,
                    step_time(maxflow, flows, (missed, t, node, remaining, n, action_time, opened | bitfornode[n], new_flow, total))
                )
            if actions < 2:
                heapq.heappush(
                    states,
                    step_time(maxflow, flows, (missed, t, node, remaining, 'IDLE', 99, opened, new_flow, total))
                )
        else:
            assert False

    print(best)


if __name__ == '__main__':
    import time

    t0 = time.monotonic()

    main("example.txt")
    t1 = time.monotonic()
    print("in ", t1 - t0)
    main("input.txt")
    t2 = time.monotonic()
    print("in ", t2 - t1)
