import aocutils


def main(file, ops, tests):
    print("RUNNING", file)
    inventory = []
    iftrue = []
    iffalse = []
    for monkey in aocutils.readsections(file):
        inventory.append(aocutils.parseints(monkey[1]))
        iftrue.append(aocutils.parseints(monkey[4])[0])
        iffalse.append(aocutils.parseints(monkey[5])[0])
    score = [0 for _ in inventory]
    for _ in range(20):
        for i in range(len(inventory)):
            inv = inventory[i]
            for item in inv:
                item = ops[i](item)
                item = item // 3
                if tests[i](item):
                    target = iftrue[i]
                else:
                    target = iffalse[i]
                inventory[target].append(item)
            score[i] += len(inv)
            inv.clear()
    score.sort(reverse=True)
    print(score[0] * score[1])


if __name__ == '__main__':
    main("example.txt",
         [
             lambda x: x * 19,
             lambda x: x + 6,
             lambda x: x * x,
             lambda x: x + 3,
         ],
         [
             lambda x: x % 23 == 0,
             lambda x: x % 19 == 0,
             lambda x: x % 13 == 0,
             lambda x: x % 17 == 0,
         ],
         )
    main("input.txt",
         [
             lambda x: x * 7,
             lambda x: x + 5,
             lambda x: x * x,
             lambda x: x + 4,
             lambda x: x * 17,
             lambda x: x + 7,
             lambda x: x + 6,
             lambda x: x + 3,
         ],
         [
             lambda x: x % 3 == 0,
             lambda x: x % 11 == 0,
             lambda x: x % 7 == 0,
             lambda x: x % 2 == 0,
             lambda x: x % 19 == 0,
             lambda x: x % 5 == 0,
             lambda x: x % 17 == 0,
             lambda x: x % 13 == 0,
         ],
         )
