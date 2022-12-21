import aocutils


def main(file):
    print("RUNNING", file)
    instructions = {}
    numbers = {}

    for line in aocutils.readlines(file):
        m, op = line.split(': ')
        if op.isnumeric():
            numbers[m] = int(op)
        else:
            instructions[m] = op

    def num(monkey):
        if monkey in numbers:
            return numbers[monkey]
        else:
            return eval_monkey(monkey)

    def eval_monkey(monkey):
        inst = instructions[monkey]
        a, op, b, = inst.split(' ')
        an = num(a)
        bn = num(b)
        if op == '+':
            res = an + bn
        elif op == '-':
            res = an - bn
        elif op == '*':
            res = an * bn
        elif op == '/':
            res = an / bn
        numbers[monkey] = res
        return res

    print(round(num('root')))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
