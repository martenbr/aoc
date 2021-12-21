from collections import defaultdict

import aocutils

outcomes_dict = defaultdict(int)
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            outcomes_dict[i + j + k] += 1
turn_outcomes = list(outcomes_dict.items())
assert sum(times for roll, times in turn_outcomes) == 27


def next_square(square, roll):
    return ((square + roll - 1) % 10) + 1


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    p1 = int(lines[0][-1])
    p2 = int(lines[1][-1])
    game_states = {(p1, p2, 0, 0): 1}
    p1_wins = 0
    p2_wins = 0
    while game_states:
        game_states, new_p1_wins = play_turn(game_states, 1)
        p1_wins += new_p1_wins

        game_states, new_p2_wins = play_turn(game_states, 2)
        p2_wins += new_p2_wins

    print(p1_wins, p2_wins)
    print(max(p1_wins, p2_wins))


def play_turn(game_states, player):
    wins = 0
    new_states = defaultdict(int)

    for game_state, games_count in game_states.items():
        p1, p2, p1_score, p2_score = game_state
        if player == 1:
            pos = p1
            score = p1_score
        else:
            pos = p2
            score = p2_score
        for roll, roll_count in turn_outcomes:
            new_pos = ((pos + roll - 1) % 10) + 1
            new_score = score + new_pos
            if new_score >= 21:
                wins += games_count * roll_count
                continue
            if player == 1:
                new_game_state = (new_pos, p2, new_score, p2_score)
            else:
                new_game_state = (p1, new_pos, p1_score, new_score)
            new_states[new_game_state] += games_count * roll_count
    return new_states, wins


if __name__ == '__main__':
    main("example.txt")

    print("444356092776315", "expected")
    main("input.txt")
