from collections import defaultdict

import aocutils


def pattern_id(line):
    i = 0
    for c in line:
        i = i << 1
        if c == "#":
            i |= 1
    return i


class Tile:
    def __init__(self, tile_id, top, bot, left, right, inner):
        self.tile_id = tile_id
        # Pattern of the edges by direction, according to the current rotation
        self.top = top
        self.bot = bot
        self.left = left
        self.right = right
        # Content of tile (when rotated according to the directions above)
        self.inner = inner
        # neighbors list of (edge_pattern, Tile)
        self.neighbors = []

        # "Pinned edges", which edge patterns needs to be in which direction in the output for the tiles to line up with neighbors
        # rotate_inner will rotate and flip the piece as needed to line up with these
        self.topp = None
        self.botp = None
        self.leftp = None
        self.rightp = None

    def opposite_edge(self, edge):
        if edge == self.top:
            return self.bot
        elif edge == self.bot:
            return self.top
        elif edge == self.left:
            return self.right
        elif edge == self.right:
            return self.left
        else:
            assert False

    def intersecting_edge(self, other_tile):
        edges = [edge for edge, tile in self.neighbors if tile is other_tile]
        assert len(edges) == 1
        return edges[0]

    def get_neighbor(self, edge):
        current = [x for x in self.neighbors if x[0] == edge]
        if not current:
            return None
        return current[0][1]

    def unused_edge(self, exclude=None):
        used = {self.topp, self.botp, self.leftp, self.rightp, exclude}
        unused = [x for x in self.neighbors if x[0] not in used]
        assert len(unused) == 1
        return unused[0]

    def transpose(self):
        self.top, self.left = self.left, self.top
        self.bot, self.right = self.right, self.bot
        self.inner = transpose(self.inner)

    def hflip(self):
        self.top, self.bot = self.bot, self.top
        self.inner = hflip(self.inner)

    def vflip(self):
        self.left, self.right = self.right, self.left
        self.inner = vflip(self.inner)

    def rotate_inner(self):
        # Must be pinned horizontally and vertically before doing the rotation
        assert (self.topp or self.botp) and (self.leftp or self.rightp)
        # Line up top and bottom by trying various transformation
        for i in range(4):
            if self.top == self.topp or self.bot == self.botp:
                break
            if i == 0:
                self.hflip()
            elif i == 1:
                self.transpose()
            elif i == 2:
                self.hflip()
        assert self.top == self.topp or self.bot == self.botp

        if self.left == self.leftp or self.right == self.rightp:
            pass
        else:
            # Left and right does not line up, flip them
            self.vflip()
            assert self.left == self.leftp or self.right == self.rightp

    def __repr__(self):
        return f"Tile({self.tile_id})"


def build_tiles_and_find_corners(file):
    sections = list(aocutils.readsections(file))
    tiles_by_id = {}
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
        inner = []
        for line in section[2:-1]:
            inner.append(line[1:-1])
        assert len(inner) == len(inner[0])
        # Edges are represents by an int with a bit pattern describing the shape
        # Since the reverse pattern is the same we use the smaller of the two possible representation (when seen as an int)
        #   min(pattern_id("##..#"), pattern_id(reversed("##..#")))
        # = min(pattern_id("##..#"), pattern_id(         "#..##"))
        # = min(         0b_11001,                     0b_10011)
        # = min(25,  19)
        # = 19
        top = min(pattern_id(top), pattern_id(reversed(top)))
        bot = min(pattern_id(bot), pattern_id(reversed(bot)))
        left = min(pattern_id(left), pattern_id(reversed(left)))
        right = min(pattern_id(right), pattern_id(reversed(right)))
        tile = Tile(tile_id, top, bot, left, right, inner)
        tiles_by_id[tile_id] = tile
        tile_by_pattern[top].append(tile)
        tile_by_pattern[bot].append(tile)
        tile_by_pattern[left].append(tile)
        tile_by_pattern[right].append(tile)
    counts = defaultdict(int)
    for tile_id in [tiles[0].tile_id for tiles in tile_by_pattern.values() if len(tiles) == 1]:
        counts[tile_id] = counts[tile_id] + 1
    corners = [tiles_by_id[tile_id] for tile_id, cnt in counts.items() if cnt == 2]
    assert len(corners) == 4
    for pattern, tiles in tile_by_pattern.items():
        if len(tiles) == 2:
            tiles[0].neighbors.append((pattern, tiles[1]))
            tiles[1].neighbors.append((pattern, tiles[0]))
    return corners


def main(file):
    print("RUNNING", file)
    corners = build_tiles_and_find_corners(file)
    # Place tiles in a grid, starting with one of the corner pieces
    # TODO clean up this mess
    first = corners[0]
    edge, _ = first.neighbors[0]
    edge = first.opposite_edge(edge)
    prev_line = None
    line = [first]
    grid = [line]
    row = 0
    prev = first
    line_first = first
    while True:
        column = 1
        while True:
            edge = prev.opposite_edge(edge)
            current = prev.get_neighbor(edge)
            if not current:
                break
            line.append(current)
            prev.rightp = edge
            current.leftp = edge
            if prev_line:
                above = prev_line[column]
                e = above.intersecting_edge(current)
                current.topp = e
                above.botp = e
            prev = current
            column += 1
        if len(grid) == len(line):
            break
        top_edge, new_line_first = line_first.unused_edge()
        line_first.botp = top_edge
        new_line_first.topp = top_edge
        bottom_edge = new_line_first.opposite_edge(top_edge)
        right_edge, _ = new_line_first.unused_edge(exclude=bottom_edge)
        edge = new_line_first.opposite_edge(right_edge)
        prev = new_line_first
        prev_line = line
        line = [new_line_first]
        grid.append(line)
        line_first = new_line_first
        row += 1

    # Rotate tiles to match desired orientations
    for row in grid:
        for tile in row:
            tile.rotate_inner()

    # Stitch images together
    full_image = []
    for tile_line in grid:
        for i in range(8):
            line = "".join("".join(t.inner[i]) for t in tile_line)
            full_image.append(line)
    # Find the sea monsters
    detect_monsters(full_image)


def transpose(data):
    # Matrix transpose (by abusing zip)
    return list(zip(*data))


def hflip(data):
    # Flip across the horizontal axis (swapping top and bot)
    return list(reversed(data))


def vflip(data):
    # Flip across the vertical axis (swapping left and right)
    return [list(reversed(d)) for d in data]


def monster_pattern(monster):
    offsets = []
    for x, line in enumerate(monster):
        for y, char in enumerate(line):
            if char == "#":
                offsets.append((x, y))
    return offsets


def list_of_strings(data):
    return ["".join(e) for e in data]


def monster_patterns():
    # Generate all 8 different transformation of the monster image
    transformations = []

    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    transformations.append(monster_pattern(monster))
    monster = hflip(monster)
    transformations.append(monster_pattern(monster))
    monster = list_of_strings(vflip(monster))
    transformations.append(monster_pattern(monster))
    monster = hflip(monster)
    transformations.append(monster_pattern(monster))

    monster = list_of_strings(transpose(monster))
    transformations.append(monster_pattern(monster))
    monster = hflip(monster)
    transformations.append(monster_pattern(monster))
    monster = list_of_strings(vflip(monster))
    transformations.append(monster_pattern(monster))
    monster = hflip(monster)
    transformations.append(monster_pattern(monster))
    return transformations


def detect_monsters(lines):
    patterns = monster_patterns()
    occupied = set()
    is_monster = set()
    size = len(lines)
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "#":
                occupied.add((x, y))
    for x in range(size):
        for y in range(size):
            for pattern in patterns:
                monster_cords = {(x + dx, y + dy) for dx, dy in pattern}
                if monster_cords.issubset(occupied):
                    is_monster.update(monster_cords)

    print(len(occupied) - len(is_monster))


if __name__ == '__main__':
    main("example.txt")
    print("RUNNING example2.txt (detect_monsters only)")
    detect_monsters(list(aocutils.readlines("example2.txt")))
    main("input.txt")
