import aocutils


def main(file):
    print("RUNNING", file)
    program = []
    for line in aocutils.readlines(file):
        inst, a = line.split(" ")
        a = int(a)
        program.append((inst, a))

    acc, run = run_program(program)
    for i in run:
        old = program[i]
        prev, num = old
        if prev == "nop":
            replace = ("jmp", num)
            program[i] = replace
        elif prev == "jmp":
            replace = ("nop", num)
            program[i] = replace
        else:
            continue
        try:
            run_program(program)
            program[i] = old
        except Done as e:
            print(e.acc)
            return


class Done(Exception):
    def __init__(self, acc):
        self.acc = acc


def run_program(program):
    acc = 0
    run = set()
    i = 0
    while True:
        if i in run:
            break
        if i == len(program):
            raise Done(acc)
        run.add(i)
        inst, num = program[i]
        if inst == "nop":
            i += 1
        elif inst == "acc":
            acc += num
            i += 1
        elif inst == "jmp":
            i += num
        else:
            assert False
    return acc, run


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
