import aocutils


def reverse_loop_size(subject, expected):
    loop_size = 0
    v = 1
    while True:
        loop_size += 1
        v = v * subject
        v = v % 20201227
        if v == expected:
            break

    return loop_size


def transform_subject(subject, loop_size):
    v = 1
    for _ in range(loop_size):
        v = v * subject
        v = v % 20201227
    return v


def main(file):
    print("RUNNING", file)
    pub1, pub2 = list(aocutils.readlines(file))
    pub1 = int(pub1)
    pub2 = int(pub2)
    priv1 = reverse_loop_size(7, pub1)
    priv2 = reverse_loop_size(7, pub2)
    x = transform_subject(pub1, priv2)
    y = transform_subject(pub2, priv1)
    assert x == y
    print(x)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
