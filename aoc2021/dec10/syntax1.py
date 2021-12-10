import aocutils

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def main(file):
    print("RUNNING", file)
    error_score = 0
    for line in aocutils.readlines(file):
        stack = []
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
                    error_score += scoring[char]
                    break
    print(error_score)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
