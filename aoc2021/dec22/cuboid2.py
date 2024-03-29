import dataclasses

import aocutils


@dataclasses.dataclass
class Cuboid:
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
    actions = []
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
        new_actions = []
        for prev_action_type, c in actions:
            if prev_action_type == 'on':
                if overlap_cuboid := overlap(c, cuboid):
                    new_actions.append(('off', overlap_cuboid))
                    total -= size(overlap_cuboid)
            elif prev_action_type == 'off':
                if overlap_cuboid := overlap(c, cuboid):
                    new_actions.append(('on', overlap_cuboid))
                    total += size(overlap_cuboid)
        actions.extend(new_actions)

        # All cubes in cuboid are now off, turn them on if this was an 'on' action
        if action_type == 'on':
            actions.append(('on', cuboid))
            total += size(cuboid)
    print(len(actions))
    print(total)


if __name__ == '__main__':
    main("example0.txt")
    print(39, "?")
    main("example_part2.txt")
    print(2758514936282235, "?")
    main("input.txt")
