import aocutils
from fractions import Fraction


class Poly:
    # Polynomial of shape ax + b
    def __init__(self, a, b):
        assert isinstance(a, Fraction)
        assert isinstance(b, Fraction)
        self.a = a
        self.b = b

    def __add__(self, other):
        assert not isinstance(other, Poly)
        return Poly(self.a, self.b + round(other))

    def __sub__(self, other):
        assert not isinstance(other, Poly)
        return Poly(self.a, self.b - round(other))

    def __mul__(self, other):
        assert not isinstance(other, Poly)
        return Poly(self.a * round(other), self.b * round(other))

    def __truediv__(self, other):
        assert not isinstance(other, Poly)
        return Poly(self.a / round(other), self.b / round(other))


def main(file):
    print("RUNNING", file)
    instructions = {}
    numbers = {}
    root = []

    for line in aocutils.readlines(file):
        m, op = line.split(': ')
        if m == 'humn':
            continue
        if m == 'root':
            a, _, b = op.split(' ')
            root.append(a)
            root.append(b)
            continue
        if op.isnumeric():
            numbers[m] = int(op)
        else:
            instructions[m] = op

    def num(monkey):
        if monkey in numbers:
            return Fraction(numbers[monkey], 1)
        elif monkey == 'humn':
            return Poly(Fraction(1, 1), Fraction(0, 1))
        else:
            return eval_monkey(monkey)

    def eval_monkey(monkey):
        inst = instructions[monkey]
        a, op, b, = inst.split(' ')
        left = num(a)
        right = num(b)

        if op == '+':
            if isinstance(right, Poly):
                res = right + left
            else:
                res = left + right
        elif op == '-':
            if isinstance(right, Poly):
                res = right * -1 + left
            else:
                res = left - right
        elif op == '*':
            if isinstance(right, Poly):
                res = right * left
            else:
                res = left * right
        elif op == '/':
            if isinstance(right, Poly):
                assert False
            else:
                res = left / right
        numbers[monkey] = res
        return res

    expr: Poly = num(root[0])
    num = num(root[1])
    my_number = (num - expr.b) / expr.a
    print(my_number)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
