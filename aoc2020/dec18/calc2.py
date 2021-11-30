import aocutils
import pyparsing as pp

grammar = pp.infixNotation(pp.Word(pp.nums), [
    ("+", 2, pp.opAssoc.LEFT),
    ("*", 2, pp.opAssoc.LEFT),
])


def eval_parsed(parsed):
    left = parsed[0]
    if isinstance(left, str):
        val = int(left)
    else:
        val = eval_parsed(left)
    for i in range(1, len(parsed), 2):
        op = parsed[i]
        right = parsed[i + 1]
        if isinstance(right, str):
            v = int(right)
        else:
            v = eval_parsed(right)
        if op == "*":
            val *= v
        elif op == "+":
            val += v
        else:
            assert False
    return val


def evaluate(expr):
    parsed = grammar.parseString(expr)[0]
    val = eval_parsed(parsed)
    return val


def main(file):
    print("RUNNING", file)
    result = 0
    for line in aocutils.readlines(file):
        val = evaluate(line)
        # print(val)
        result += val
    print(result)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
