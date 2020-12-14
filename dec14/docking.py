import aocutils


def main(file):
    print("RUNNING", file)
    # 10X
    # (0b111 & 0b101) | 0b100 = 0x101
    # (0b000 & 0b101) | 0b100 = 0x100
    memory = {}
    and_mask = 0
    or_mask = 0
    for line in aocutils.readlines(file):

        if line.startswith("mask"):
            pattern = line.split(" = ")[1]
            and_mask = 0
            or_mask = 0
            for c in pattern:
                and_mask = and_mask << 1
                or_mask = or_mask << 1
                if c == "X":
                    and_mask |= 1
                elif c == "1":
                    and_mask |= 1
                    or_mask |= 1
                elif c == "0":
                    pass
                else:
                    assert False
        else:
            parts = aocutils.multisplit(line, ["[", "]", " = "])
            address = int(parts[1])
            value = int(parts[-1])
            write_value = (value & and_mask) | or_mask
            memory[address] = write_value
    print(sum(memory.values()))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
