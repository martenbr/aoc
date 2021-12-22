import dataclasses
from collections import defaultdict
from typing import NamedTuple

import aocutils


class Cuboid(NamedTuple):
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int


def overlap(a: Cuboid, b: Cuboid):
    x0 = max(a.x0, b.x0)
    y0 = max(a.y0, b.y0)
    z0 = max(a.z0, b.z0)
    x1 = min(a.x1, b.x1)
    y1 = min(a.y1, b.y1)
    z1 = min(a.z1, b.z1)
    if x0 > x1 or y0 > y1 or z0 > z1:
        return None
    return Cuboid(x0, x1, y0, y1, z0, z1)


def size(a: Cuboid):
    return (1 + a.x1 - a.x0) * (1 + a.y1 - a.y0) * (1 + a.z1 - a.z0)


def main(file):
    print("RUNNING", file)
    on_actions = defaultdict(int)
    off_actions = defaultdict(int)
    total = 0
    for line in aocutils.readlines(file):
        parts = aocutils.multisplit(line, [' x=', '..', ',y=', '..', ',z=', '..'])
        action_type = parts[0]
        x0, x1, y0, y1, z0, z1 = [int(a) for a in parts[1:]]
        assert x0 <= x1
        assert y0 <= y1
        assert z0 <= z1
        cuboid = Cuboid(x0, x1, y0, y1, z0, z1)
        # Turn off all cubes inside the cuboid by doing
        # the inverse of all actions so far, but only in the
        # intersection with the cuboid
        prev_actions = []
        for k, v in on_actions.items():
            for _ in range(v):
                prev_actions.append(('on', k))
        for k, v in off_actions.items():
            for _ in range(v):
                prev_actions.append(('off', k))
        for prev_action_type, c in prev_actions:
            if prev_action_type == 'on':
                if overlap_cuboid := overlap(c, cuboid):
                    if not try_remove_cuboid(on_actions, overlap_cuboid):
                        off_actions[overlap_cuboid] += 1
                    total -= size(overlap_cuboid)
            elif prev_action_type == 'off':
                if overlap_cuboid := overlap(c, cuboid):
                    if not try_remove_cuboid(off_actions, overlap_cuboid):
                        on_actions[overlap_cuboid] += 1
                    total += size(overlap_cuboid)

        # All cubes in cuboid are now off, turn them on if this was an 'on' action
        if action_type == 'on':
            if not try_remove_cuboid(off_actions, cuboid):
                on_actions[cuboid] += 1
            total += size(cuboid)

    print(len(on_actions) + len(off_actions))
    print(total)


def try_remove_cuboid(actions, overlap_cuboid):
    if overlap_cuboid in actions:
        count = actions[overlap_cuboid]
        if count == 1:
            actions.pop(overlap_cuboid)
        else:
            actions[overlap_cuboid] -= 1
        return True
    return False


if __name__ == '__main__':
    main("example0.txt")
    print(39, "?")
    main("example_part2.txt")
    print(2758514936282235, "?")
    main("input.txt")
