required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
]


def main():
    passport = {}
    count = 0
    for line in open("input.txt"):
        line = line.strip()
        if line == "":
            if all(k in passport for k in required):
                count += 1
            passport = {}
            continue
        for field in line.split(" "):
            k, v = field.split(':')
            passport[k] = v
    print(count)


if __name__ == '__main__':
    main()
