class Node:
    def __init__(self, cup):
        self.next: Node = None
        self.cup = cup


class CircularLinkedList:
    def __init__(self, cups):
        nodes_by_cup = {}
        first = Node(cups[0])
        nodes_by_cup[first.cup] = first
        prev = first
        for c in cups[1:]:
            current = Node(c)
            nodes_by_cup[current.cup] = current
            prev.next = current
            prev = current
        current.next = first
        self.node_by_cup = nodes_by_cup

    def find_cup_node(self, cup) -> Node:
        return self.node_by_cup[cup]

    def insert_after(self, after: Node, nodes):
        start = after
        end = after.next
        start.next = nodes[0]
        nodes[-1].next = end

    def remove_after(self, before_node: Node, count):
        nodes = []
        n = before_node
        for i in range(count):
            n = n.next
            nodes.append(n)

        after_node = n.next
        n.next = None
        before_node.next = after_node
        return nodes

    def as_list_starting_with(self, cup):
        result = []
        first = self.node_by_cup[cup]
        n = first
        while True:
            result.append(n.cup)
            n = n.next
            if n.cup == cup:
                break
        return result


def play(cups, moves):
    size = len(cups)
    ll = CircularLinkedList(cups)
    current_node = ll.find_cup_node(cups[0])
    for p in range(moves):
        picked_nodes = ll.remove_after(current_node, 3)
        picked_cups = set(n.cup for n in picked_nodes)

        destination_cup = current_node.cup - 1
        while True:
            if destination_cup == 0:
                destination_cup += size
            if destination_cup not in picked_cups:
                break
            destination_cup -= 1
        destination_node = ll.find_cup_node(destination_cup)
        ll.insert_after(destination_node, picked_nodes)
        current_node = current_node.next
    return ll.as_list_starting_with(1)


def main(input, moves, part2=True):
    print("RUNNING", input, "(part2)" if part2 else "(part1)")

    cups = [int(c) for c in input]
    if part2:
        for c in range(10, 1000001):
            cups.append(c)
        assert len(cups) == 1_000_000
    cups = play(cups, moves)
    if part2:
        print(cups[1], cups[2])
        print(cups[1] * cups[2])
    else:
        print(cups)
        print("".join(str(c) for c in cups[1:]))


if __name__ == '__main__':
    main("389125467", moves=100, part2=False)
    main("362981754", moves=100, part2=False)
    main("389125467", moves=10_000_000)
    main("362981754", moves=10_000_000)
