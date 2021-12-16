import math

import aocutils


class Op:
    def __init__(self, type, subp):
        self.type = type
        self.subp = subp

    def apply(self):
        sub_results = [p.apply() for p in self.subp]
        if self.type == 0:
            return sum(sub_results)
        elif self.type == 1:
            return math.prod(sub_results)
        elif self.type == 2:
            return min(sub_results)
        elif self.type == 3:
            return max(sub_results)
        elif self.type == 5:
            assert len(sub_results) == 2
            if sub_results[0] > sub_results[1]:
                return 1
            else:
                return 0
        elif self.type == 6:
            assert len(sub_results) == 2
            if sub_results[0] < sub_results[1]:
                return 1
            else:
                return 0
        elif self.type == 7:
            assert len(sub_results) == 2
            if sub_results[0] == sub_results[1]:
                return 1
            else:
                return 0


class Lit:
    def __init__(self, value):
        self.value = value

    def apply(self):
        return self.value


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
        return Lit(result)
    else:
        # Operator
        length_type = reader.read_bits(1)
        sub_packets = []
        if length_type == 1:
            length = reader.read_bits(11)
            for _ in range(length):
                sub_packets.append(parse(reader))
        else:
            length = reader.read_bits(15)
            packet_end = reader.consumed_bits + length
            while reader.consumed_bits < packet_end:
                sub_packets.append(parse(reader))
            assert reader.consumed_bits == packet_end
        return Op(type, sub_packets)


def main(file):
    print("RUNNING", file)
    for line in aocutils.readlines(file):
        data = bytes.fromhex(line)
        packet = parse(BitReader(data))
        print(packet.apply())


if __name__ == '__main__':
    print(parse(BitReader(bytes.fromhex("C200B40A82"))).apply())
    print("==3")
    print(parse(BitReader(bytes.fromhex("04005AC33890"))).apply())
    print("==54")
    print(parse(BitReader(bytes.fromhex("880086C3E88112"))).apply())
    print("==7")
    print(parse(BitReader(bytes.fromhex("CE00C43D881120"))).apply())
    print("==9")
    print(parse(BitReader(bytes.fromhex("D8005AC2A8F0"))).apply())
    print("==1")
    print(parse(BitReader(bytes.fromhex("F600BC2D8F"))).apply())
    print("==0")
    print(parse(BitReader(bytes.fromhex("9C005AC2F8F0"))).apply())
    print("==0")
    print(parse(BitReader(bytes.fromhex("9C0141080250320F1802104A08"))).apply())
    print("==1")
    main("input.txt")
