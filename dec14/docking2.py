import aocutils


class Mask:
    def __init__(self):
        self.and_mask = 0
        self.or_mask = 0

    def apply(self, value):
        return (value & self.and_mask) | self.or_mask

    def push_force1(self):
        self.and_mask = self.and_mask << 1
        self.or_mask = self.or_mask << 1
        self.and_mask |= 1
        self.or_mask |= 1

    def push_force0(self):
        self.and_mask = self.and_mask << 1
        self.or_mask = self.or_mask << 1

    def push_unchanged(self):
        self.and_mask = self.and_mask << 1
        self.or_mask = self.or_mask << 1
        self.and_mask |= 1

    def both(self):
        copy = Mask()
        copy.and_mask = self.and_mask
        copy.or_mask = self.or_mask
        self.push_force0()
        copy.push_force1()
        return copy


def main(file):
    print("RUNNING", file)
    memory = {}
    masks = []
    for line in aocutils.readlines(file):
        if line.startswith("mask"):
            pattern = line.split(" = ")[1]
            masks = [Mask()]
            for c in pattern:
                if c == "X":
                    new_masks = []
                    for mask in masks:
                        new_masks.append(mask.both())
                    masks.extend(new_masks)
                elif c == "1":
                    for mask in masks:
                        mask.push_force1()
                elif c == "0":
                    for mask in masks:
                        mask.push_unchanged()
                else:
                    assert False
        else:
            parts = aocutils.multisplit(line, ["[", "]", " = "])
            address = int(parts[1])
            value = int(parts[-1])
            for mask in masks:
                a = mask.apply(address)
                memory[a] = value
    print(sum(memory.values()))


if __name__ == '__main__':
    # main("example.txt")
    main("example2.txt")
    main("input.txt")
