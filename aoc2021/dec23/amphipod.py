import aocutils
import heapq

room_positions = [2, 4, 6, 8]
allowed_hallway_locations = [x for x in range(11) if x not in room_positions]

move_costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

char_goals = dict(zip('ABCD', room_positions))


def moves(state, room_size):
    hallway, rooms = state
    room_dict = dict(zip(room_positions, rooms))
    # room -> hallway
    for x, room in room_dict.items():
        if room:
            char = room[-1]
            if x == char_goals[char] and all(c == char for c in room):
                continue
            char_cost = move_costs[char]
            y = room_size + 1 - len(room)
            for xd in allowed_hallway_locations:
                if not all(x == '.' for x in hallway[min(x, xd):max(x, xd) + 1]):
                    continue
                yield char, char_cost * (y + abs(x - xd)), (x, y), (xd, 0)
    # hallway -> room
    for x, char in enumerate(hallway):
        if char == '.':
            continue
        char_cost = move_costs[char]
        xd = char_goals[char]
        room = room_dict[xd]
        if not all(c == char for c in room):
            continue
        if not all(x == '.' for x in hallway[min(x, xd) + 1:max(x, xd)]):
            continue

        yd = room_size - len(room)
        yield char, char_cost * (yd + abs(x - xd)), (x, 0), (xd, yd)


def tuple_push(tup, elem):
    new = list(tup)
    new.append(elem)
    return tuple(new)


def tuple_pop(tup):
    return tup[:-1]


def do_move(state, move):
    hallway, rooms = state
    char, cost, (x, y), (xd, yd) = move
    if y == 0:
        # From hallway
        new_hallway = ''.join('.' if i == x else c for i, c in enumerate(hallway))
        new_rooms = tuple(tuple_push(room, char) if i == xd else room for i, room in zip(room_positions, rooms))

    elif yd == 0:
        # Into hallway
        new_hallway = ''.join(char if i == xd else c for i, c in enumerate(hallway))
        new_rooms = tuple(tuple_pop(room) if i == x else room for i, room in zip(room_positions, rooms))
    else:
        assert False
    return new_hallway, new_rooms


def main(file, part2=False):
    print("RUNNING", file)
    lines = []
    for line in aocutils.readlines(file):
        lines.append(line)
    top = lines[2][3:10].split('#')
    bot = lines[3][3:10].split('#')

    hallway = '.' * 11
    rooms = [[] for _ in range(4)]
    if part2:
        rows = [top, 'DCBA', 'DBAC', bot]
        room_size = 4
    else:
        rows = [top, bot]
        room_size = 2
    for row in reversed(rows):
        for i, char in enumerate(row):
            rooms[i].append(char)
    rooms = tuple(tuple(room) for room in rooms)
    visited = set()
    state = (hallway, rooms)
    queue = [(0, state)]
    while queue:
        current_cost, state = heapq.heappop(queue)
        if state in visited:
            continue
        visited.add(state)
        all_moves = list(moves(state, room_size))
        if not all_moves and state[0] == '...........':
            # print_state(state, room_size)
            print(current_cost)
            return
        for move in all_moves:
            new_state = do_move(state, move)
            new_cost = move[1]
            heapq.heappush(queue, (current_cost + new_cost, new_state))


def print_state(state, room_size):
    hallway, rooms = state
    print(hallway)
    room_dict = dict(zip(room_positions, rooms))
    for y in range(room_size - 1, -1, -1):
        for i in range(11):
            if i not in room_dict:
                print(' ', end='')
                continue
            room = room_dict[i]
            if len(room) > y:
                print(room[y], end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    main("example.txt")
    print(12521, "?")
    main("input.txt")
    print()
    print("PART2")
    main("example.txt", True)
    print(44169, "?")
    main("input.txt", True)
