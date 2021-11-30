import re

required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_field(k, v: str):
    if k == 'byr':
        return len(v) == 4 and v.isdigit() and "1920" <= v <= "2002"
    elif k == 'iyr':
        return len(v) == 4 and v.isdigit() and "2010" <= v <= "2020"
    elif k == 'eyr':
        return len(v) == 4 and v.isdigit() and "2020" <= v <= "2030"
    elif k == 'hgt':
        if v.endswith("cm"):
            v = v[:-2]
            return len(v) == 3 and v.isdigit() and "150" <= v <= "193"
        elif v.endswith("in"):
            v = v[:-2]
            return len(v) == 2 and v.isdigit() and "59" <= v <= "76"
        else:
            return False
    elif k == 'hcl':
        return re.match(r"^#[0-9a-f]{6}$", v)
    elif k == 'ecl':
        return v in colors
    elif k == 'pid':
        return re.match(r"^[0-9]{9}$", v)
    assert False


def validate_passport(passport):
    if not all(k in passport for k in required):
        return False
    for k in required:
        if k in passport:
            v = passport[k]
            if not check_field(k, v):
                return False
    return True


def main():
    passport = {}
    count = 0
    for line in open("input.txt"):
        line = line.strip()
        if line == "":
            if validate_passport(passport):
                count += 1
            passport = {}
            continue
        for field in line.split(" "):
            k, v = field.split(':')
            passport[k] = v
    if validate_passport(passport):
        count += 1
    print(count)


if __name__ == '__main__':
    main()
