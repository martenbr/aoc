import aocutils


class Node:
    def __init__(self, num):
        self.next: Node = None
        self.prev: Node = None
        self.num = num


class CircularLinkedList:
    def __init__(self, nums):
        nodes_by_index = {}
        first = Node(nums[0])
        nodes_by_index[0] = first
        prev = first
        for i, c in enumerate(nums[1:]):
            current = Node(c)
            if c == 0:
                self.zero_node = current
            nodes_by_index[i + 1] = current
            prev.next = current
            current.prev = prev
            prev = current
        current.next = first
        first.prev = current
        self.node_by_orig_index = nodes_by_index

    def find_num(self, idx) -> Node:
        return self.node_by_orig_index[idx]

    def insert_after(self, left: Node, node):
        assert left is not node
        right = left.next
        left.next = node
        node.next = right
        right.prev = node
        node.prev = left

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def as_list_starting_with_0(self):
        result = []
        first = self.zero_node
        n = first
        while True:
            result.append(n.num)
            n = n.next
            if n is first:
                break
        return result


def main(file):
    print("RUNNING", file)
    nums = list(int(x) for x in aocutils.readlines(file))
    nums = [x * 811589153 for x in nums]
    ll = CircularLinkedList(nums)
    start = ll.find_num(0)
    n = start
    while True:
        assert n.prev
        assert n.next
        if n is start:
            break
    for _ in range(10):
        for i, num in enumerate(nums):
            n = ll.find_num(i)
            target = n
            if num == 0:
                continue

            ll.remove(n)
            if num > 0:
                moves = num % (len(nums) - 1)
                for _ in range(moves):
                    target = target.next
            elif num < 0:
                moves = abs(num) % (len(nums) - 1)
                for _ in range(moves + 1):
                    target = target.prev

            ll.insert_after(target, n)

    mixed = ll.as_list_starting_with_0()
    n1 = mixed[1000 % len(mixed)]
    n2 = mixed[2000 % len(mixed)]
    n3 = mixed[3000 % len(mixed)]
    print(n1 + n2 + n3, n1, n2, n3)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
