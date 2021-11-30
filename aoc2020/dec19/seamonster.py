import aocutils


class Literal:
    def __init__(self, char):
        assert len(char) == 1
        self.char = char

    def matches(self, msg, next_index):
        if msg[next_index] == self.char:
            yield next_index + 1


class Ref:
    def __init__(self, rules, refs):
        self.rules = rules
        assert len(refs) in [1, 2, 3]
        self.refs = refs

    def matches(self, msg, next_index):
        if len(self.refs) == 1:
            for n in self.rules[self.refs[0]].matches(msg, next_index):
                yield n
        elif len(self.refs) == 2:
            for n in self.rules[self.refs[0]].matches(msg, next_index):
                for n2 in self.rules[self.refs[1]].matches(msg, n):
                    yield n2
        elif len(self.refs) == 3:
            for n in self.rules[self.refs[0]].matches(msg, next_index):
                for n2 in self.rules[self.refs[1]].matches(msg, n):
                    for n3 in self.rules[self.refs[2]].matches(msg, n2):
                        yield n3


class Opt:
    def __init__(self, rules, refs1, refs2):
        self.o1 = Ref(rules, refs1)
        self.o2 = Ref(rules, refs2)

    def matches(self, msg, next_index):
        for n1 in self.o1.matches(msg, next_index):
            yield n1
        for n2 in self.o2.matches(msg, next_index):
            yield n2


def main(file):
    print("RUNNING", file)
    sections = list(aocutils.readsections(file))
    rules = {}
    for line in sections[0]:
        key, match = line.split(": ")
        key = int(key)

        if '"' in match:
            rules[key] = Literal(match.strip('"'))
        elif "|" in match:
            r1, r2 = match.split(" | ")
            refs1 = [int(r) for r in r1.split(" ")]
            refs2 = [int(r) for r in r2.split(" ")]
            rules[key] = Opt(rules, refs1, refs2)
        else:
            refs = [int(r) for r in match.split(" ")]
            rules[key] = Ref(rules, refs)
    start_rule = rules[0]
    matches = 0
    for line in sections[1]:
        for match_length in start_rule.matches(line, 0):
            if match_length == len(line):
                matches += 1
                break
    print(matches)


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
