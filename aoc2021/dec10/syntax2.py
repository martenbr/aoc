import aocutils

scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def main(file):
    print("RUNNING", file)
    incomplete_score = []
    for line in aocutils.readlines(file):
        stack = []
        corrupted = False
        for char in line:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif char == '<':
                stack.append('>')
            else:
                expected = stack.pop()
                if char != expected:
                    corrupted = True
                    break
        if corrupted:
            continue

        line_score = 0
        while stack:
            expected = stack.pop()
            line_score = line_score * 5 + scoring[expected]
        incomplete_score.append(line_score)
    incomplete_score.sort()
    print(incomplete_score[len(incomplete_score) // 2])


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
