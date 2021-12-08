import aocutils

segments_by_digit = [
    'abcefg',  # 0
    'cf',  # 1
    'acdeg',  # 2
    'acdfg',  # 3
    'bcdf',  # 4
    'abdfg',  # 5
    'abdefg',  # 6
    'acf',  # 7
    'abcdefg',  # 8
    'abcdfg',  # 9
]

shared_segments = {}
for d1 in range(10):
    for d2 in range(10):
        shared_segments[(d1, d2)] = len(set(segments_by_digit[d1]).intersection(segments_by_digit[d2]))


def main(file):
    print("RUNNING", file)
    total = 0
    for line in aocutils.readlines(file):
        line_split = line.split(' | ')
        signal_digits = [''.join(sorted(digit)) for digit in line_split[0].split(' ')]
        output_digits = [''.join(sorted(digit)) for digit in line_split[1].split(' ')]
        all_digits = signal_digits + output_digits
        mappings = {}
        # Assign initial choices based on number of segments
        for digit in all_digits:
            digit = ''.join(sorted(digit))
            if digit in mappings:
                continue
            segments = len(digit)
            if segments == 2:
                possible_choices = {1}
            elif segments == 3:
                possible_choices = {7}
            elif segments == 4:
                possible_choices = {4}
            elif segments == 7:
                possible_choices = {8}
            elif segments == 5:
                possible_choices = {2, 3, 5}
            elif segments == 6:
                possible_choices = {0, 6, 9}
            else:
                assert False
            mappings[digit] = possible_choices

        # Reduce choices for uncertain mappings based on amount of segments shared with already known mappings
        while True:
            if all(len(mappings[d]) == 1 for d in output_digits):
                break
            for digit in all_digits:
                possible_choices = mappings[digit]
                if len(possible_choices) == 1:
                    continue
                for other_digit, other_digit_choices in mappings.items():
                    if digit == other_digit:
                        continue
                    if len(other_digit_choices) == 1:
                        other_mapped_to = list(other_digit_choices)[0]
                        for assumed in list(possible_choices):
                            expected_shared = len(set(digit).intersection(set(other_digit)))
                            if shared_segments[assumed, other_mapped_to] != expected_shared:
                                # The amount of shared segments does not match assumed, it is not a valid choice
                                mappings[digit].discard(assumed)
        total += int(''.join([str(list(mappings[x])[0]) for x in output_digits]))
    print("total", total)


if __name__ == '__main__':
    main("example.txt")
    main("example2.txt")
    main("input.txt")
