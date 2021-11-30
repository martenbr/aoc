if __name__ == '__main__':
    valid = 0
    for line in open("input.txt"):
        parts = line.split(" ")
        a, b = parts[0].split("-")
        a = int(a)
        b = int(b)
        char = parts[1][0]
        password = parts[2].strip()
        count = 0
        for c in password:
            if c == char:
                count += 1
        pos1 = password[a - 1] == char
        pos2 = password[b - 1] == char
        if (pos1 and not pos2) or (not pos1 and pos2):
            valid += 1
            print("valid  ", line)
        else:
            print("invalid", line)

    print(valid)
