from collections import deque

import aocutils


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    deck1 = deque(int(x) for x in sections[0][1:])
    deck2 = deque(int(x) for x in sections[1][1:])
    while deck1 and deck2:
        c1 = deck1.popleft()
        c2 = deck2.popleft()
        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c1 < c2:
            deck2.append(c2)
            deck2.append(c1)
        else:
            assert False

    winning_deck = list(deck1 or deck2)
    print(winning_deck)
    print(sum([x * (i + 1) for i, x in enumerate(reversed(winning_deck))]))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
