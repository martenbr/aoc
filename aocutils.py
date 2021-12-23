from typing import List


def readsections(file):
    return sections_from_lines(open(file))


def readlines(file):
    for line in open(file):
        yield line.strip('\r\n')


def multisplit(line: str, tokens: List[str]):
    rest = line
    parts = []
    for t in tokens:
        p1, rest = rest.split(t, 1)
        parts.append(p1)
    parts.append(rest)
    return parts


def sections_from_lines(lines):
    section = []
    for line in lines:
        line = line.strip()
        if line == "":
            yield section
            section = []
        else:
            section.append(line)
    if section:
        yield section
