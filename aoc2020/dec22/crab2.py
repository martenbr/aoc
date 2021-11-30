from collections import deque

import aocutils


class P1Win(Exception):
    def __init__(self, deck):
        self.deck = deck


class P2Win(Exception):
    def __init__(self, deck):
        self.deck = deck


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    deck1 = deque(int(x) for x in sections[0][1:])
    deck2 = deque(int(x) for x in sections[1][1:])
    _, winning_deck = recursive_combat(deck1, deck2)
    winning_deck = list(winning_deck)

    print(winning_deck)
    print(sum([x * (i + 1) for i, x in enumerate(reversed(winning_deck))]))


def recursive_combat(deck1, deck2):
    seen_states = set()
    while deck1 and deck2:
        current_state = tuple(deck1)
        if current_state in seen_states:
            return 1, deck1
        seen_states.add(current_state)

        c1 = deck1.popleft()
        c2 = deck2.popleft()
        if c1 <= len(deck1) and c2 <= len(deck2):
            winner, _ = recursive_combat(
                deque(list(deck1)[:c1]),
                deque(list(deck2)[:c2]),
            )
        else:
            if c1 > c2:
                winner = 1
            elif c1 < c2:
                winner = 2
            else:
                assert False
        if winner == 1:
            deck1.append(c1)
            deck1.append(c2)
        elif winner == 2:
            deck2.append(c2)
            deck2.append(c1)
    if deck1:
        return 1, deck1
    if deck2:
        return 2, deck2
    assert False


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
