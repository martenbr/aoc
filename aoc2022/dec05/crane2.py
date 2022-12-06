import aocutils


def main(file):
    print("RUNNING", file)
    init, inst = list(aocutils.readsections(file))
    nstacks = (len(init[-1]) +2) // 4
    stacks = {}
    for i in range(nstacks):
        stacks[i+1] = []
    for l in reversed(init[:-1]):
        for i in range(nstacks):
            try:
                c = l[i*4+1]
            except IndexError:
                c = ' '
            if c != ' ':
                stacks[i+1].append(c)
    for ins in inst:
        cnt, fr, to = aocutils.parseints(ins)
        crane = []
        for _ in range(cnt):
            if stacks[fr]:
                crane.append(stacks[fr].pop())
        while crane:
            stacks[to].append(crane.pop())

    print(''.join(s[-1] for s in stacks.values()))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
