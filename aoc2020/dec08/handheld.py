import aocutils


def main(file):
    print("RUNNING", file)
    program = []
    for line in aocutils.readlines(file):
        inst, a = line.split(" ")
        a = int(a)
        program.append((inst, a))

    acc = 0
    run = set()
    i = 0
    while True:
        if i in run:
            break
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
    print(acc)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
