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
        if a <= count <= b:
            valid += 1
            print("valid  ", line)
        else:
            print("invalid", line)

    print(valid)
