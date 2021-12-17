import aocutils


def print_binary(d):
    print("{0:b}".format(d))


def get_bits(data, start, num):
    byte_offset, bit_offset = divmod(start, 8)
    result = 0
    remaining = num
    while remaining:
        result = result << 1
        if bit_offset == 8:
            byte_offset += 1
            bit_offset = 0
        if data[byte_offset] & (1 << (7 - bit_offset)) == 0:
            pass
        else:
            result |= 1
        remaining -= 1
        bit_offset += 1
    return result


class BitReader:
    def __init__(self, data):
        self.data = data
        self.consumed_bits = 0

    def read_bits(self, num):
        result = get_bits(self.data, self.consumed_bits, num)
        self.consumed_bits += num
        return result


def parse(reader: BitReader):
    version = reader.read_bits(3)
    type = reader.read_bits(3)
    if type == 4:
        # Literal
        result = 0
        more = True
        while more:
            result = result << 4
            more = reader.read_bits(1) == 1
            b = reader.read_bits(4)
            result = result | b
        return version
    else:
        # Operator
        length_type = reader.read_bits(1)
        sub_versions = 0
        if length_type == 1:
            length = reader.read_bits(11)
            for _ in range(length):
                sub_versions += parse(reader)
        else:
            length = reader.read_bits(15)
            packet_end = reader.consumed_bits + length
            while reader.consumed_bits < packet_end:
                sub_versions += parse(reader)
            assert reader.consumed_bits == packet_end

        return version + sub_versions


def main(file):
    print("RUNNING", file)
    for line in aocutils.readlines(file):
        data = bytes.fromhex(line)
        version_sum = parse(BitReader(data))
        print(version_sum)


if __name__ == '__main__':
    main("example1.txt")
    print("==16")
    main("example2.txt")
    print("==12")
    main("example3.txt")
    print("==23")
    main("example4.txt")
    print("==31")
    main("input.txt")
