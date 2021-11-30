import aocutils


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    fields = []
    for line in sections[0]:
        name, a, b, c, d = aocutils.multisplit(line, [": ", "-", " or ", "-"])

        fields.append([
            name,
            (int(a), int(b)),
            (int(c), int(d)),
        ])
    invalid = []
    for line in sections[2][1:]:
        values = [int(x) for x in line.split(",")]
        for v in values:
            valid = False
            for _, (a, b), (c, d) in fields:
                if a <= v <= b or c <= v <= d:
                    valid = True
                    break

            if not valid:
                invalid.append(v)
    print(invalid)
    print(sum(invalid))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
