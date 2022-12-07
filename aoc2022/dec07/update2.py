import aocutils


class Dir:
    def __init__(self):
        self.files = []
        self.subdirs = []

    def size(self):
        return sum(self.files) + sum(d.size() for d in self.subdirs)


def main(file):
    print("RUNNING", file)
    lines = list(aocutils.readlines(file))
    tree = {}
    path = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("$ ls"):
            p = '/'.join(path)
            d = tree.setdefault(p, Dir())
            files = []
            subdirs = []
            while True:
                i += 1
                if i == len(lines) or lines[i][0] == '$':
                    break
                else:
                    if lines[i][0:3] == 'dir':
                        subp = '/'.join(path + [lines[i][4:]])
                        subdirs.append(tree.setdefault(subp, Dir()))
                    else:
                        files.append(int(lines[i].split(' ')[0]))
            d.files = files
            d.subdirs = subdirs
        else:
            line = lines[i]
            assert line.startswith('$ cd')
            d = line.split(' ')[2]
            if d == '..':
                path.pop()
            elif d == '/':
                path = []
            else:
                path.append(d)
            i += 1
    foo = []
    for v in tree.values():
        foo.append(v.size())
    foo.sort()
    used = tree[''].size()
    remaining = 70_000_000 - used
    needed = 30_000_000 - remaining
    for v in foo:
        if v > needed:
            print(v)
            break



if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
