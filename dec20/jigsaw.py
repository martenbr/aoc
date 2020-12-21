from collections import defaultdict

import aocutils


def pattern_id(line):
    i = 0
    for c in line:
        i = i << 1
        if c == "#":
            i |= 1
    return i


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    tile_by_pattern = defaultdict(list)
    for section in sections:
        tile_id = int(aocutils.multisplit(section[0], [" ", ":"])[1])
        top = section[1]
        bot = section[-1]
        left = []
        right = []
        for line in section[1:]:
            left.append(line[0])
            right.append(line[-1])
        top = min(pattern_id(top), pattern_id(reversed(top)))
        bot = min(pattern_id(bot), pattern_id(reversed(bot)))
        left = min(pattern_id(left), pattern_id(reversed(left)))
        right = min(pattern_id(right), pattern_id(reversed(right)))
        tile_by_pattern[top].append(tile_id)
        tile_by_pattern[bot].append(tile_id)
        tile_by_pattern[left].append(tile_id)
        tile_by_pattern[right].append(tile_id)

    counts = defaultdict(int)
    tile_ids_for_unmatched_edges = [tiles[0] for tiles in tile_by_pattern.values() if len(tiles) == 1]
    for tile_id in tile_ids_for_unmatched_edges:
        counts[tile_id] = counts[tile_id] + 1
    corners = [tile_id for tile_id, cnt in counts.items() if cnt == 2]
    print(corners)
    print(corners[0] * corners[1] * corners[2] * corners[3])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
