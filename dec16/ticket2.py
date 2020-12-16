import aocutils


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    fields = []
    for line in sections[0]:
        field_name, a, b, c, d = aocutils.multisplit(line, [": ", "-", " or ", "-"])

        fields.append((
            field_name,
            (int(a), int(b)),
            (int(c), int(d)),
        ))
    valid_tickets = []
    for line in sections[2][1:]:
        values = [int(x) for x in line.split(",")]
        ticket_valid = True
        for v in values:
            if not any(is_valid(f, v) for f in fields):
                ticket_valid = False
                break

        if ticket_valid:
            valid_tickets.append(values)

    possible_fields = []

    for v in valid_tickets[0]:
        possible_fields.append({f[0] for f in fields if is_valid(f, v)})

    for i in range(len(possible_fields)):
        p = possible_fields[i]
        for t in valid_tickets[1:]:
            v = t[i]
            valids = {f[0] for f in fields if is_valid(f, v)}
            p.intersection_update(valids)
    print(possible_fields)

    while True:
        solved = []
        not_solved = []
        for p in possible_fields:
            if len(p) == 1:
                solved.append(list(p)[0])
            else:
                not_solved.append(p)
        if not not_solved:
            break
        for p in not_solved:
            p.difference_update(solved)
    print(possible_fields)

    own_values = [int(x) for x in sections[1][1].split(",")]
    result = 1
    for i in range(len(possible_fields)):
        field_name = list(possible_fields[i])[0]
        if field_name.startswith("departure "):
            result *= own_values[i]

    print(result)


def is_valid(field, v):
    _, (a, b), (c, d) = field
    if a <= v <= b or c <= v <= d:
        return True
    return False


if __name__ == '__main__':
    main("example.txt")
    main("example2.txt")
    main("input.txt")
