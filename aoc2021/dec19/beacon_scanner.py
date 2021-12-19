import aocutils
import itertools

rotations = []


def mk_rotate(a, b, c, asign, bsign, csign):
    return lambda cord: (cord[a] * asign, cord[b] * bsign, cord[c] * csign)


for a, b, c in itertools.permutations(range(3)):
    for asign in [-1, 1]:
        for bsign in [-1, 1]:
            for csign in [-1, 1]:
                rotations.append(mk_rotate(a, b, c, asign, bsign, csign))


def check_rotations():
    variants = set()
    for rotate in rotations:
        rotated = rotate((1, 2, 3))
        assert rotated not in variants
        variants.add(rotated)
    assert len(variants) == 48

    for x in variants:
        variants2 = set()
        for rotate in rotations:
            rotated = rotate(x)
            assert rotated not in variants2
            variants2.add(rotated)
        assert variants == variants2


def main(file):
    check_rotations()
    print("RUNNING", file)
    scanners = []
    for sec_lines in aocutils.readsections(file):
        scanner = []
        for line in sec_lines[1:]:
            scanner.append(tuple(int(x) for x in line.split(',')))
        scanners.append(scanner)
    # Scanner ID is their index in 'scanners'

    searched = set()
    offsets = {
        0: (0, 0, 0)
    }
    to_search = [0]
    while to_search:
        progress = (len(searched) + len(offsets)) * 50 / len(scanners)
        print(f'{round(progress)}%')
        if len(offsets) == len(scanners):
            break
        s1_id = to_search.pop()
        assert s1_id not in searched
        searched.add(s1_id)

        s1 = scanners[s1_id]
        s1_set = set(s1)
        for s2_id, s2 in enumerate(scanners):
            if s1_id == s2_id:
                continue
            if s2_id in offsets:
                continue
            for rotate in rotations:
                rotated_s2 = [rotate(x) for x in s2]
                if offset := scanners_overlaps(s1_set, rotated_s2):
                    scanners[s2_id] = rotated_s2
                    offsets[s2_id] = (
                        offsets[s1_id][0] + offset[0],
                        offsets[s1_id][1] + offset[1],
                        offsets[s1_id][2] + offset[2],
                    )
                    to_search.append(s2_id)
                    break

    assert len(offsets) == len(scanners)

    print("part1")
    beacons = set()
    for sec_id, scanner in enumerate(scanners):
        for cord in scanner:
            beacons.add((
                offsets[sec_id][0] + cord[0],
                offsets[sec_id][1] + cord[1],
                offsets[sec_id][2] + cord[2],
            ))
    print(len(beacons))

    print("part2")
    maxd = 0
    for i in range(len(scanners)):
        for j in range(i, len(scanners)):
            dist = (
                    abs(offsets[i][0] - offsets[j][0]) +
                    abs(offsets[i][1] - offsets[j][1]) +
                    abs(offsets[i][2] - offsets[j][2])
            )
            maxd = max(maxd, dist)
    print(maxd)


def scanners_overlaps(s1_set, rotated_s2):
    for s1_cord in s1_set:
        for s2_cord in rotated_s2:
            # Assuming s1_cord and s2_cord represent the same coordinate, check how much the scanner images overlap
            overlap = 0
            xoff = s1_cord[0] - s2_cord[0]
            yoff = s1_cord[1] - s2_cord[1]
            zoff = s1_cord[2] - s2_cord[2]
            for x, y, z in rotated_s2:
                cord = (x + xoff, y + yoff, z + zoff)
                if cord in s1_set:
                    overlap += 1
            if overlap >= 12:
                return xoff, yoff, zoff
    return None


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
